import functools
from flask import Flask,render_template, request
from flask_mysqldb import MySQL
from flask import Flask
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
bp = Blueprint('auth', __name__, url_prefix='/auth')

app = Flask(__name__)
#- criando a conexao com o banco
mysql = MySQL(app)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'eductech'

# -- routes
@app.route('/')
def home():
    return render_template('home.html')
          
@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')
    
@app.route('/posts')
def posts():
    return render_template('posts.html')

@app.route('/tarefas')
def tarefas():
    return render_template('tarefas.html')

@app.route('/cadastrar_aluno')
def cadastroAluno():
    return render_template('cadastroAluno.html')

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

@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == 'POST': 
        try: 
            nome = request.form['nome']
            cpf = request.form['cpf']
            rg = request.form['rg']
            dt_nasc = request.form['nascimento']
            sexo = request.form['sexo']
            end = request.form['endereco']
            tel = request.form['telefone']
            email = request.form['email']
            senha = request.form['senha']
            nm_pai =  request.form['nome_pai']
            nm_mae =  request.form['nome_mae']
            #insertForm = ("INSERT INTO eductech.cadastro_aluno (nome, senha) VALUES (%s, %s)", (nome,senha))
            cursor2 = mysql.connection.cursor()
            cursor2.execute(
                "INSERT INTO eductech.cadastro_aluno (Nome, RG, CPF, Data_Nascimento, Sexo, Nome_pai, Nome_mae, Endereco, Telefone, email, senha) VALUES (%s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                (nome,rg, cpf, dt_nasc, sexo, nm_pai, nm_mae, end, tel, email, senha))
            mysql.connection.commit()
            return render_template('home.html')
        except:
            return render_template('cadastroAluno.html')

@app.route('/cadastrar_professor')
def cadastroProfessor():
    return render_template('cadastroProfessor.html')

@app.route('/calendario')
def calendario():
    return render_template('calendar.html')

# @app.route('/login-aluno')
# def loginAluno():
    # return render_template('')
if __name__ == '__main__':
    app.run(debug=True)

""" @bp.route('/register', methods=('GET', 'POST'))
def register():
    return render_template('auth/register.html') """
