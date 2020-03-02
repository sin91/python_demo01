#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    # return '<h1>Home</h1>'
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def sigin_form():
    # return '''<form action ="/signin" method="post">
    #             <p>User Name:<input name="username" /></p>
    #             <p>Password:<input name="password" /></p>
    #             <p><button type="submit">Sign In</button></p>
    #            </form>
    #         '''
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    # Read fields from form
    if username.strip() == 'admin' and password.strip() == '123456':
        # return '<h3>Hello, admin!</h3>'
        return render_template('signin-ok.html', username=username)
    # return '<h3>Incorrect username or password.</h3>'
    return render_template('form.html', message='Incorrect username or password', username=username)

if __name__ == '__main__':
    app.run()
