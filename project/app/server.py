import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
bp = Blueprint('auth', __name__, url_prefix='/auth')

from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')
    
@app.route('/posts')
def posts():
    return render_template('posts.html')

if __name__ == '__main__':
    app.run(debug=True)


""" @bp.route('/register', methods=('GET', 'POST'))
def register():
    return render_template('auth/register.html') """
