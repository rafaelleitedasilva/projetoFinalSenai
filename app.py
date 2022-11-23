import functools
from flask import Flask,render_template, request
from flask_mysqldb import MySQL
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
bp = Blueprint('auth', __name__, url_prefix='/auth')

app = Flask(__name__)
#- criando a conexao com o banco
mysql = MySQL(app)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'senai125_diadema'
app.config['MYSQL_PASSWORD'] = ''

app.config['MYSQL_DB'] = 'eductech'
# lists data
dados_aluno = []
cad = []
# -- routes
@app.route('/')
def home():
    return render_template('home.html')
          
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

@app.route('/perfilAluno', methods = ['POST'])
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
            print(nome, ' ----------- NOME DA PAGINA PERFIL REQUEST')
            cursor= mysql.connection.cursor()
            sql_update_qr =  """Update eductech.cadastro_aluno set Nome = %s, RG=%s, CPF=%s, Data_Nascimento=%s, Sexo=%s, email=%s, senha=%s, Nome_pai=%s, Nome_mae=%s, Endereco=%s, Telefone=%s where RA = %s""" 
            data_qr = (nome, rg, cpf, dt_nasc, sexo, email, senha, nm_pai, nm_mae, end, tel, ra_)
            cursor.execute(sql_update_qr, data_qr)
            cursor.commit()
            print(f'NUMEROS DE LINHAS AFETADAS : {cursor.rowcount}')
            cursor.close()
        except Exception as e :
            print('erro: ', e) 
    return render_template('perfilAluno.html', ra_bd = dados_aluno[0][0], nome_bd = dados_aluno[0][1] ,  rg_bd = dados_aluno[0][2] ,cpf_bd = dados_aluno[0][3],  data_nas_bd = dados_aluno[0][4] ,sexo_bd = dados_aluno[0][5], np_bd = dados_aluno[0][6], nm_bd = dados_aluno[0][7],  end_bd = dados_aluno[0][8], tel_bd = dados_aluno[0][9],  email_bd = dados_aluno[0][10] ,senha_bd = dados_aluno[0][11]) 

@app.route('/perfilProfessor')
def perfilProfessor():
    return render_template('perfilProfessor.html')   

@app.route('/posts')
def posts():
    return render_template('posts.html')

@app.route('/tarefaAcervo')
def tarefas():
    return render_template('tarefaAcervo.html')

@app.route('/login', methods = ['POST', 'GET'])
def login_screen():
    if request.method == 'POST':

        email = request.form['email']
        senha = request.form['senha']
        
        cursor= mysql.connection.cursor()
        cursor.execute("SELECT * from eductech.cadastro_aluno WHERE email = '{}' AND senha = '{}'".format(email, senha))
        dados = cursor.fetchone()
        dados_aluno.append(dados)
        print(dados, ' aqui é a pagina  do login ')
        try: 
            if dados[10]== email and dados[11] == senha:
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

if __name__ == '__main__':
    app.run(debug=True)