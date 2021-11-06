import requests, os, bs4

myUrl = "https://en.wikipedia.org/w/api.php"
parameters={"action":"query","list":"allpages","apfrom":"Mexic","aplimit":100,"format":"json"}
myData = requests.get(myUrl, params=parameters)
DATA = myData.json()
print(type(DATA))

PAGES = DATA["query"]["allpages"] #error if not exists

for page in PAGES:
    print(page["title"])
