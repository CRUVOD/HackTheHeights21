import requests, json

months={"january":"1","february":"2","march":"3","april":"4","may":"5","june":"6","july":"7","august":"8","september":"9","october":"10","november":"11","december":"12"}

def parseDate(pageText,dateType):
    global months
    dateString="error"
    dateStart = pageText.find(dateType)+len(dateType) #no b because case-insensitive start
    if(dateStart-len(dateType)==-1):
        return "error"
    dateEnd = pageText.index("\n",dateStart)#will error if no newline
    
    dateText=pageText[dateStart:dateEnd]
    dateStart=dateText.find("|")
    if(dateStart!=-1):#if well-formatted
        dateStart=dateText.find("|",dateStart)
        dateEnd=dateText.find("|",dateStart+1)
        bYear=dateText[dateStart+1:dateEnd]
        if(not bYear[0].isdigit()):
            return "error"

        dateStart=dateEnd
        dateEnd=dateText.find("|",dateStart+1)
        bMonth=dateText[dateStart+1:dateEnd]
        if(len(bMonth)<2):
            bMonth="0"+bMonth

        dateStart=dateEnd+1
        dateEnd=dateStart+2
        bDay=dateText[dateStart:dateEnd]
        if(not bDay[1].isdigit()):#one digit day and no leading 0
            bDay="0"+bDay[0]
        dateString=bYear+"-"+bMonth+"-"+bDay
    elif(dateText.find(",")!=-1):
        dateStart=dateText.find("=")
        dateEnd=dateText.find(" ",dateText.find(",")-3)#finds space between month and day
        try:
            bMonth=months[dateText[dateStart+1:dateEnd].strip().lower()]
        except:
            return "error"
        dateStart=dateEnd+1
        dateEnd=dateText.find(",")
        bDay=dateText[dateStart:dateEnd]
        dateStart=dateEnd+2
        bYear=dateText[dateStart:dateStart+4]
    else: #maybe its just the year?? will write code to parse later
        bYear=dateText[-4:]
        if(not bYear.isdigit()):
            return "error"
        bMonth="01"
        bDay="01"
    if(len(bMonth)<2):
        bMonth="0"+bMonth
    if(len(bDay)<2):
        bDay="0"+bDay
    dateString=bYear+"-"+bMonth+"-"+bDay
    return dateString

def scraperFunc(category="19th-century_Mexican_politicians"):
    #------------------
    #START OF MAIN CODE
    #------------------
    myUrl = "https://en.wikipedia.org/w/api.php"
    #parameters={"action":"query","list":"allpages","apfrom":"Mexic","aplimit":100,"format":"json"}
    #params2={"action":"query","prop":"info","inprop":"watchers"}#what pages to do on
    #pageName="Otto_von_Bismarck"
    #pageName="Stephen_F._Austin"
    #params3={"action":"parse","page":pageName,"format":"json"}

    #category="Critics_of_postmodernism" #TEST< PLEASEE REMOVE!!!!!!!!!!!!!!
    VIEWDAYS=5
    params4={"action":"query","generator":"categorymembers","gcmtitle":("Category:"+category),"gcmlimit":200,"gcmtype":"page","prop":"revisions|pageviews|description|info","rvslots":"main","rvprop":"content","pvipdays":VIEWDAYS,"inprop":"url","format":"json"}#idk rvslots
    
    myData = requests.get(myUrl, params=params4)
    DATA = myData.json()
    #print(type(DATA)) #should be dictionary

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
    #both of them end with a \n (as its a wikipedia table), so just detect when next \n

    #DATA["query"]["pages"]["2411709"]["revisions"][0]["slots"]["main"]["*"]

    myJSON={}
    dateStrings=["Birth of ","Death of ",""]
    dateTypes=["birth_date","death_date","date"]#dates we are interested in for the query, each one is a new entry
    
    for pageID in DATA["query"]["pages"]:
        myPage=DATA["query"]["pages"][pageID]
        badDate=0
        for i in range(len(dateTypes)):
            pageTitle=myPage["title"]
            pageTitle=dateStrings[i] + pageTitle
            myJSON[pageTitle]=[]
            #print(pageID)
            
            try:
                pageText = myPage["revisions"][0]["slots"]["main"]["*"]
            except:
                print("Error finding page text")
                continue

            if(dateTypes[i]!="date" or badDate>1):#date is for singular events, only check if not birth/death since generic name
                dateString=parseDate(pageText,dateTypes[i])
            
            if(dateString!="error"):
                myJSON[pageTitle].append(dateString)
            else:#idk what to do here
                print("Error in parsing",pageTitle)
                badDate+=1
                del myJSON[pageTitle]
                continue
                myJSON[pageTitle].append("3000-01-01")
            try:
                myJSON[pageTitle].append(myPage["description"])
            except:
                #print("No short description")
                myJSON[pageTitle].append(myPage["title"])#just has title as description
            try:
                viewAvg=0
                for viewday in myPage["pageviews"]:
                    if(myPage["pageviews"][viewday]==None):
                        continue
                    viewAvg+=myPage["pageviews"][viewday]
                viewAvg/=VIEWDAYS
                myJSON[pageTitle].append(viewAvg)
            except:
                #print("No pageview data")
                myJSON[pageTitle].append(5)
            myJSON[pageTitle].append(myPage["fullurl"])

    myJSON=sorted(myJSON.items(), key=lambda x:x[1][0])#python 3.6+ required
    return myJSON

#with open("dateJSON.json","w") as myFile:
#    json.dump(myJSON,myFile)
