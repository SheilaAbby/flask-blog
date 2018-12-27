from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm,LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '3638836a16e1e56ee58871cfaf32e290'
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

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm() # create a register form
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check username and passoword', 'danger')
    return render_template('login.html', title='Login', form=form)
