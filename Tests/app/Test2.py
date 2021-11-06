from flask import Flask, request
from flask import render_template


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
    content1 = [processed_text,'title2','title3','title4']
    content2 = ['Body1','Body2','Body3','Body4']
    dates = ['12/1',
                '2/1',
                '7/4',
                '8/4']
    return render_template('index.html', 
                           title='Welcome', 
                           dates=dates,
                           content1=content1,
                           content2=content2)

app.run(host='0.0.0.0', port=81)

