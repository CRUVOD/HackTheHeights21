from flask import Flask, request
from flask import render_template

import Scraper

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    content1 = ['']
    content2 = ['']
    dates = ['']
    return render_template('index.html', 
                           title='Welcome', 
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
    a = Scraper.scraperFunc()
    
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

