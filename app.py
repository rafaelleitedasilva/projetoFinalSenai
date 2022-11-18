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
app.config['MYSQL_PASSWORD'] = 'senai125_diadema'
app.config['MYSQL_DB'] = 'eductech'
# lists data
dados_aluno = []
cad = []
# -- routes
@app.route('/')
def home():
    return render_template('home.html')
          
@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')
    
@app.route('/cadastrar_aluno')
def cadastroAluno():
    return render_template('cadastroAluno.html')

@app.route('/cadastrar_professor')
def cadastroProfessor():
    return render_template('cadastroProfessor.html')

@app.route('/calendar')
def calendario():
    return render_template('calendar.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/perfilAluno')
def perfilAluno():

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

    if request.method == 'POST': 
        try: 
            
            cursor= mysql.connection.cursor()
            # cursor.execute(f"UPDATE eductech.cadastro_aluno SET Nome = '{nome}', RG = '{rg}', CPF  = '{cpf}', Data_Nascimento = '{dt_nasc}', Sexo = '{sexo}', email = '{email}', senha = '{senha}', Nome_pai = '{nm_pai}',Nome_mae = '{nm_mae}', Endereco = '{end}', Telefone = '{tel}' WHERE RA = '{dados_aluno[0][0]}'")    
            ra_ = 1
            cursor.execute("""
       UPDATE eductech.cadastro_aluno
       SET RA = %s Nome=%s, RG=%s, CPF=%s, Data_Nascimento=%s, Sexo=%s, email=%s, senha=%s, Nome_pai=%s, Nome_mae=%s, Endereco=%s, Telefone=%s
       WHERE RA=%s
    """, (ra_, nome, rg, cpf, dt_nasc, sexo, email, senha, nm_pai, nm_mae, end, tel, ra_))
            cursor.commit()
            print(f'NUMEROS DE LINHAS AFETADAS : {cursor.rowcount}')
            cursor.close()
        except:
            print('erro') 
    return render_template('perfilAluno.html', ra_bd = dados_aluno[0][0], nome_bd = dados_aluno[0][1] ,  rg_bd = dados_aluno[0][2] ,cpf_bd = dados_aluno[0][3],  data_nas_bd = dados_aluno[0][4] ,sexo_bd = dados_aluno[0][5], np_bd = dados_aluno[0][6], nm_bd = dados_aluno[0][7],  end_bd = dados_aluno[0][8], tel_bd = dados_aluno[0][9],  email_bd = dados_aluno[0][10] ,senha_bd = dados_aluno[0][11]) 

@app.route('/perfilProfessor')
def perfilProfessor():
    return render_template('perfilProfessor.html')   

@app.route('/posts')
def posts():
    return render_template('posts.html')

@app.route('/tarefas')
def tarefas():
    return render_template('tarefas.html')

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
            cursor2 = mysql.connection.cursor()
            cursor2.execute(
                "INSERT INTO eductech.cadastro_aluno (Nome, RG, CPF, Data_Nascimento, Sexo, Nome_pai, Nome_mae, Endereco, Telefone, email, senha) VALUES (%s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                (nome,rg, cpf, dt_nasc, sexo, nm_pai, nm_mae, end, tel, email, senha))
            mysql.connection.commit()
            cad.append(email)
            cad.append(senha)

            return render_template('login.html')
        except:
            print('deu erro')
            return render_template('cadastroAluno.html')

if __name__ == '__main__':
    app.run(debug=True)