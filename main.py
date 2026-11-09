from flask import Flask, render_template, redirect, session, request
from app.database import *
from datetime import timedelta

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/Myblog'

app.secret_key = 'ih213i4ih1465hkjd-14325413-1324dsftg1-3214twedsf'
# app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)
# app.url_map.strict_slashes = False
init_db(app)

@app.route("/")
def home_page():
    return render_template('index.html', posts = get_posts())

@app.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        myUser = request.form['username']
        myPassword = request.form['password']
        if myUser == 'Admin' and myPassword == '1234': 
            session['user_name'] = 'Behnood'
            session['Logged in'] = True
            return redirect('/')
    return render_template('login.html')

@app.route("/newpost", methods = ['GET', 'POST'])
def new_post():
    import os
    import time

    if request.method == 'POST':
        myTitle = request.form['title']
        myContent = request.form['content']

        myImage = None
        if 'image' in request.files and request.files['image'].filename != '':
            file =  request.files['image']
            filename = f'{time.time()}-{file.filename}'
            filePath = os.path.join('static', 'uploads', 'image', filename)
            file.save(filePath)
            myImage = filename

        add_post(myTitle, myContent, myImage)
        return redirect('/')

    return render_template('newpost.html')

@app.route("/logout")
def logout():
    session.pop('user_name')
    session.pop('Logged in')
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug = True)