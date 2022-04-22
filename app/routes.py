from app import app
from flask import flash, redirect, render_template, url_for

from app.forms import LoginForm
@app.route('/')
@app.route('/index')
def index():
    user = {'kullaniciadi': 'Cisco Python TT'}
    gonderiler = [
        {
            'yazar':"Cisco",
            'baslik':"Python",
            'icerik':"Python ile Cisco'a Python'ınızı kullanın"
        },
        { 'yazar':"Cisco",
            'baslik':"Python",
            'icerik':"Python ile Cisco'a Python'ınızı kullanın"
        },
    ] 
    # baslik = 'Cisco Python TT'
    return render_template('home.html', baslik="", user=user,gonderiler=gonderiler)

# @app.route("/login")
# def login():
#     form = LoginForm()
#     return render_template('login.html',title='Sign In', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)