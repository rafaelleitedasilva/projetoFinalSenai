import functools
from flask import Flask,render_template, request
from flask_mysqldb import MySQL
from flask import Flask
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
bp = Blueprint('auth', __name__, url_prefix='/auth')


app = Flask(__name__)
# - criando a conexao com o banco
mysql = MySQL(app)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'eductech'

# -- routes
@app.route('/')
def home():
    return render_template('home.html')

# @app.route('/teste_db') # , methods = ['POST', 'GET']
# def teste():
#     cur = mysql.connection.cursor()
#     cur.execute('Select * from eductech.teste_post')
#     fetchdata = cur.fetchall()
#     cur.close()
#     return render_template('teste_db.html', data= fetchdata)

@app.route('/login', methods = ['POST', 'GET'])
def login_screen():
    if request.method == 'POST':

        email = request.form['email']
        senha = request.form['senha']
        
        cursor= mysql.connection.cursor()
        cursor.execute("SELECT * from eductech.cadastro_aluno WHERE email = '{}' AND senha = '{}'".format(email, senha))
        dados = cursor.fetchone()

        print(dados)
        try: 
            if dados[14]== email and dados[15] == senha:
                return redirect(url_for('home'))  
        except:
                msg = 'erro'
                return render_template('login.html', data=msg)
                
    return render_template('login.html')
          


@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')
    
@app.route('/posts')
def posts():
    return render_template('posts.html')

@app.route('/tarefas')
def tarefas():
    return render_template('tarefas.html')


if __name__ == '__main__':
    app.run(debug=True)



""" @bp.route('/register', methods=('GET', 'POST'))
def register():
    return render_template('auth/register.html') """
