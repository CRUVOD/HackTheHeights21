from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    content1 = 'Lorem'
    content2 = 'Body'
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

