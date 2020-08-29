from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ff766e854ac9c0d99911c5d28c6389e2'

posts = [
    {
        'author' : 'Anusua Dey',
        'title' : 'Blog Post'
    },
    {
        'author' : 'Shubhamay Das',
        'title' : 'Blog Post'
    }
]

# Decorator
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods= ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit() :
        flash(f'Account Created for {form.user_name.data}!', 'success')
        redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == "__main__":
    app.run(debug=True)

