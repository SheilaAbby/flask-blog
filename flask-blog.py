from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author':'Corey Schafer',
        'title':'post 1',
        'content':'First post comment',
        'date_posted':'April 21,2018'
    },
    {
        'author':'Sheila Kioko',
        'title':'post 2',
        'content':'second post comment',
        'date_posted':'April 20,2019'
    }
]

@app.route('/')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About Us')
