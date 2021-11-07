from flask import Flask, request
from flask import render_template

import Scraper
import difflib

app = Flask(__name__)

approvedList = ["19th-century_Canadian_politicians",
                "Jazz_accordionists",
                "Critics_of_postmodernism",
               " Scientists_from_Boston",
               "19th-century_Mexican_politicians"]

@app.route('/')
@app.route('/index')
def index():
    content1 = ['']
    content2 = ['']
    dates = ['']
    return render_template('index.html', 
                           title='Hack The Heights', 
                           dates=dates,
                           content1=content1,
                           content2=content2)

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.strip()
    title = []
    content = []
    dates = []
    print(difflib.get_close_matches(processed_text, approvedList,1,0)[0])
    a = Scraper.scraperFunc(difflib.get_close_matches(processed_text, approvedList,1,0)[0])
    
    for item in a:
        title.append(item[0])
        dates.append(item[1][0])
        content.append(item[1][1])
        
    
    return render_template('index.html', 
                           title='Welcome', 
                           dates=dates,
                           content1=title,
                           content2=content)

app.run(host='0.0.0.0', port=81)

