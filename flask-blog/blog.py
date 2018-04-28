#this is the controller for the web app

#imports
import sqlite3

from flask import Flask, render_template, request, session, flash, redirect, url_for, g

#configuration

DATABASE = "blog.db"

app = Flask(__name__)

#pull app configuration by looking for UPPERCASE vars
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/main')
def main():
    return render_template("main.html")

if __name__ == '__main__':
    app.run(debug=True)