import functools
from flask import Flask,render_template, request, flash
from flask_mysqldb import MySQL
from flask_socketio import SocketIO, emit
from werkzeug.utils import secure_filename
import os
import urllib.request

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
bp = Blueprint('auth', __name__, url_prefix='/auth')

app = Flask(__name__)

app.secret_key = "emanuel-gatao"

io = SocketIO(app)

#- criando a conexao com o banco
mysql = MySQL(app)
# app.config['MYSQL_HOST'] = 'us-cdbr-east-06.cleardb.net'
# app.config['MYSQL_USER'] = 'bee0845ec95fd8'
# app.config['MYSQL_PASSWORD'] = 'senai125_diadema'
# app.config['MYSQL_PASSWORD'] = '1f0584b3'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''

app.config['MYSQL_DB'] = 'eductech'
# lists data        
dados_aluno = []
dados_prof = []
usr = []

# - 

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
  
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'pdf'])
  
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# -- routes
@app.route('/')
def login():
    return render_template('login.html')

@app.route('/home')  
def home():
    usuario = get_user()
    print(dados_prof)
    print('---------- ')
    print(dados_aluno)
    return render_template('home.html', usuario = usuario)

@app.route('/cadastrar_aluno')
def cadastroAluno():
    return render_template('cadastroAluno.html')

@app.route('/cadastrar_professor')
def cadastroProfessor():
    return render_template('cadastroProfessor.html')

@app.route('/calendar')
def calendario():
    return render_template('calendar.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/perfilAluno', methods = ['POST', 'GET'])
def perfilAluno():
    print(dados_aluno)
    ra_ = dados_aluno[0][0]
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
            cursor= mysql.connection.cursor()
            
            sql_update_qr =  """Update eductech.cadastro_aluno set Nome = %s, RG=%s, CPF=%s, Data_Nascimento=%s, Sexo=%s,Nome_pai=%s, Nome_mae=%s, Endereco=%s, Telefone=%s, email=%s, senha=%s where RA = %s""" 
            data_qr = (nome, rg, cpf, dt_nasc, sexo, nm_pai, nm_mae, end, tel, email, senha, ra_)
            cursor.execute(sql_update_qr, data_qr)

            mysql.connection.commit()
            cursor.close()
        except Exception as e :
            print('erro: ', e) 
    return render_template('perfilAluno.html', ra_bd = dados_aluno[0][0], nome_bd = dados_aluno[0][1] ,  rg_bd = dados_aluno[0][2] ,cpf_bd = dados_aluno[0][3],  data_nas_bd = dados_aluno[0][4] ,sexo_bd = dados_aluno[0][5], np_bd = dados_aluno[0][6], nm_bd = dados_aluno[0][7],  end_bd = dados_aluno[0][8], tel_bd = dados_aluno[0][9],  email_bd = dados_aluno[0][10] ,senha_bd = dados_aluno[0][11]) 

@app.route('/perfilProfessor')
def perfilProfessor():
    print(dados_prof)
    nif = dados_prof[0][0]
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
            formacao =  request.form['formacao']
            disc =  request.form['disc']
            cursor= mysql.connection.cursor()
            
            sql_update_qr =  """Update eductech.cadastro_professor set Nome = %s, RG=%s, CPF=%s, Data_Nascimento=%s, Sexo=%s, Endereco=%s, Telefone=%s, email=%s, senha=%s, Nome_Disciplina, Formacao where nif = %s""" 
            data_qr = (nome, rg, cpf, dt_nasc, sexo, end, tel, email, senha,disc, formacao, nif)
            cursor.execute(sql_update_qr, data_qr)

            mysql.connection.commit()
            cursor.close()
        except Exception as e :
            print('erro: ', e) 
    return render_template('perfilProfessor.html', nif = dados_prof[0][0],nome_bd = dados_prof[0][1], cpf_bd = dados_prof[0][4], rg_bd = dados_prof[0][5],sexo_bd = dados_prof[0][7], data_nas_bd = dados_prof[0][3], end_bd = dados_prof[0][6], tel_bd = dados_prof[0][8], form_bd = dados_prof[0][2], disc_bd = dados_prof[0][2],  email_bd = dados_prof[0][9], senha_bd = dados_prof[0][10] )


@app.route('/acervo-de-materiais-didaticos')
def acervo():
    print(usr, ' asjasijas ias jasi jasijias jas jias ijasisa')
    divs = get_data()
    usuario = get_user()
    print(usuario, 'usuario tela acervo     ')
    return render_template('acervo.html', divs = divs, usuario = usuario)

def get_data():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * from acervo')
    rows = cursor.fetchall()    
    return rows

def get_user():         
    if usr[0] == 'professor':
        usur = 'professor'
        return usur
    elif usr[0] == 'aluno':
        usur = 'aluno'  
        return usur

@app.route('/inserir-material')
def insert_screen():
    return render_template('send_files.html')

@app.route('/upload_acervo', methods = ['POST', 'GET'])
def upload_acervo():
    
    cur = mysql.connection.cursor()
    if request.method == 'POST':

        desc = request.form['descricao-material']
        disc =  request.form['disciplina']

        professor =  dados_prof[0][1] 
        # print(professor)

        files = request.files.getlist('files[]')
        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

                cur.execute("INSERT INTO acervo (file_name, descricao, disciplina, professor) VALUES (%s, %s, %s, %s)",[filename, desc, disc, professor ])
                mysql.connection.commit()
            print(file)
        cur.close()   
    return redirect('/acervo-de-materiais-didaticos')

@app.route('/tarefas')
def tarefas():
    return render_template('tarefas.html')

@app.route('/login', methods = ['POST', 'GET'])
def login_screen():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        cursor= mysql.connection.cursor()
        
        if 'professor' in email:
            cursor.execute("SELECT * from eductech.cadastro_professor WHERE email = '{}' AND senha = '{}'".format(email, senha))
            dados = cursor.fetchone()
            dados_prof.append(dados)
            usr.append('professor')
            print(dados_prof)
            try: 
                if dados[9]== email and dados[10] == senha:
                    print('login de professor')  
                    return redirect(url_for('home'))
                else: 
                    msg = 'login nao confere'
                return render_template('login.html', data=msg)

            except Exception as e:
                msg = 'erro '                
                return render_template('login.html', data=msg, erro = e)
        elif 'aluno' in email:
            cursor.execute("SELECT * from eductech.cadastro_aluno WHERE email = '{}' AND senha = '{}'".format(email, senha))
            dados = cursor.fetchone()
            dados_aluno.append(dados)
            usr.append('aluno')
            try: 
                if dados[10]== email and dados[11] == senha:
                    print('login de aluno')  
                    return redirect(url_for('home'))  
                else: 
                    msg = 'login nao confere'
                    return render_template('login.html', data=msg)
            except Exception as e:
                    msg = 'erro '                
                    return render_template('login.html', data=msg, erro = e)
                
    return render_template('login.html')

@app.route('/insert', methods = ['POST'])
def insertAluno():
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
            cursor2 = mysql.connection.cursor()
            cursor2.execute(
                "INSERT INTO eductech.cadastro_aluno (Nome, RG, CPF, Data_Nascimento, Sexo, Nome_pai, Nome_mae, Endereco, Telefone, email, senha) VALUES (%s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                (nome,rg, cpf, dt_nasc, sexo, nm_pai, nm_mae, end, tel, email, senha))
            mysql.connection.commit()
            return render_template('login.html')
            
        except:
            print('deu erro')
            return render_template('cadastroAluno.html')

@app.route('/insertprof', methods=['POST'])
def insertProfessor():
    if request.method == 'POST': 
        try:
            nome = request.form['nome']
            cpf = request.form['cpf']
            rg = request.form['rg']
            dt_nasc = request.form['nascimento']
            sexo = request.form['sexo']
            end = request.form['endereco']
            formacao = request.form['formacao']
            disciplina = request.form['disc']
            tel = request.form['telefone']
            email = request.form['email']
            senha = request.form['senha']

            cursor = mysql.connection.cursor()
            cursor.execute(
                "INSERT INTO eductech.cadastro_professor (Nome, Formacao, Data_Nascimento,CPF, RG, Endereco, Sexo, Telefone, Email, Senha, Nome_Disciplina) VALUES (%s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                (nome,formacao, dt_nasc,cpf, rg, end, sexo,tel, email, senha, disciplina)
            )
            mysql.connection.commit()
            return render_template('login.html')
            
        except Exception as e:
            print(f'deu erro {e}')
            return render_template('cadastroProfessor.html')

@io.on('sendMessage')
def send_message_handler(msg):
    emit('getMessage', msg, broadcast=True)

if __name__ == '__main__':
    io.run(app, debug=True)