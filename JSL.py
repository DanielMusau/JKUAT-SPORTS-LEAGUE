from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY']= 'd622c7f03f8d461da5d5b211e316ba30'


Teams = ["Mavetto FC", "AWFC", "Chelton FC"]


@app.route('/') 
@app.route('/home')
def home():
    return render_template("home.html", teams=Teams)

@app.route('/about') 
def about():
    return render_template("about.html",  title= 'About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form= LoginForm()
    return render_template('login.html', title='login', form=form)

if __name__ == '__main__':
    app.run()