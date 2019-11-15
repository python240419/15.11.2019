# first - import flask from Settings
from flask import Flask
from flask import render_template, request, redirect,url_for

app = Flask(__name__)

@app.route('/')
def home_page():
    name = 'itay'
    return f'<html><h1><b>Welcome to flask! {name}</b></h1></html>'

@app.route('/again')
def again_page():
    return f'<hr>again...<br><hr>'

app.run()
