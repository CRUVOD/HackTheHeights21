import requests, os, bs4

myUrl = "https://en.wikipedia.org/w/api.php"
parameters={"action":"query","list":"allpages","apfrom":"Mexic","aplimit":100,"format":"json"}
params2={"action":"query","prop":"info","inprop":"watchers"}#what pages to do on
#pageName="Otto_von_Bismarck"
pageName="Stephen_F._Austin"
params3={"action":"parse","page":pageName,"format":"json"}
category="19th-century_Mexican_politicians"
params4={"action":"query","generator":"categorymembers","gcmtitle":("Category:"+category),"prop":"revisions","rvslots":"*","rvprop":"content","format":"json"}#idk rvslots
         #"prop":"pageviews" #pageviews returns views for past n days

myData = requests.get(myUrl, params=params4)
DATA = myData.json()
print(type(DATA)) #should be dictionary

#PAGES = DATA["query"]["allpages"] #error if not exists

'''
#params3
pageText = DATA["parse"]["text"]["*"]

#actually parsing the stuff
dateStart = pageText.index("<span class=\"bday")+19
print(pageText[dateStart:dateStart+10])

#for page in PAGES:

'''
#params4
#apparently the wikitext isn't fully standardized for birth date, fails on Stephen F. Austin
#one way is |birth_date = MNAME MDAY, 4YEAR
#other was is |birth_date = {{birth date|1792|2|18|mf=y}}
#both of them end with a \n (as its a wikipedia table, so just detect when next \n
DATA["query"]["pages"]["2411709"]["revisions"][0]["slots"]["main"]["*"]

myJSON={"events",[]}
for pageID in DATA["query"]["pages"]:
    pageText = DATA["query"]["pages"][pageID]["revisions"][0]["slots"]["main"]["*"]
    dateStart = pageText.find("birth_date")+10 #no b because case-insensitive start
    if(dateStart-10==-1):
        print("ERROR at pageID=",pageID)
        continue
    dateEnd = pageText.index("\n",dateStart)#will error if no newline
    
    dateText=pageText[dateStart:dateEnd]
    dateStart=dateText.find("irth date|")
    if(dateStart!=-1):#if well-formatted
        dateStart=dateText.find("|",dateStart)
        dateEnd=dateText.find("|",dateStart+1)
        #print(dateText[dateStart+1:dateStart+5])
        bYear=int(dateText[dateStart+1:dateEnd])

        dateStart=dateEnd
        dateEnd=dateText.find("|",dateStart+1)
        #print(dateText[dateStart+1:dateEnd])
        bMonth=int(dateText[dateStart+1:dateEnd])

        dateStart=dateEnd
        dateEnd=dateText.find("|",dateStart+1)
        #print(dateText[dateStart+1:dateEnd])
        bDay=int(dateText[dateStart+1:dateEnd])
    #print("PAGEID=",pageID,"START:",pageText[dateStart:dateEnd],":END")
    #elif(dateText.find(",")!=-1): #later on will actually handle this
        #print("This is weird")
    

