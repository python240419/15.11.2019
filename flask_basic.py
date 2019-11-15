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

def hello_no_route():
    # will not work....
    return f'<hr>hello...<br><hr>'

@app.route('/hello/<name>')
def hello_name(name):
    return f'Hello {name}'

@app.route('/blog/<int:postID>')
def my_blog(postID):
    post = ['post one', 'second post', 'cool third post']
    return f'<hr><b>POST :</b> {post[postID]}<br><hr>'

# targil - create URL which gets 2 numbers and print their sum
# 'sum/3/4' --> will display: 3 + 4 = 7
@app.route('/sum/<int:x>/<int:y>')
def sum(x, y):
    return f'{x} + {y} = {x+y}'

@app.route('/sumf/<float:x>/<float:y>')
def sumf(x, y):
    return f'{x} + {y} = {x+y}'

@app.route('/w3')
def goto_w3():
    return redirect('https://www.w3schools.com/')

@app.route('/admin')
def hello_admin():
    return 'Hello admin'

@app.route('/user/<username>')
def hello_user(username):
    return f'Hello user : <span style="color:blue">{username}</span>'

@app.route('/login/<name>')
def hello_login(name):
    if name == 'itay':
        return redirect(url_for('hello_admin')) # redirect('/admin')
    else:
        return redirect(url_for('hello_user', username=name))

app.run()
