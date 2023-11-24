from flask import Flask, render_template, request
app = Flask(__name__)

import pymysql

db = pymysql.connect(host="127.0.0.1",
                     user="root",
                     password="aluno",
                     database="ValidaCPF")

def calcula_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))
 
    if len(cpf) != 11 or len(set(cpf)) == 1:
        return False

    v1 = 0
    v2 = 0
 
    for i in range(9):
        v1 += int(cpf[8 - i]) * (9 - (i % 10))
        v2 += int(cpf[8 - i]) * (9 - ((i + 1) % 10))

    v1 = (v1 % 11) % 10
    v2 = (v2 % 11) % 10
    

    return cpf.endswith(str(v1) + str(v2))
 
@app.route('/')
def index():
    cursor = db.cursor()
    sql = "SELECT * FROM  parceiros;"
    cursor.execute(sql)
    parceiros = cursor.fetchall()
    return render_template('index.html', parceiros=parceiros)

@app.route('/validar_cpf', methods=['post'])
def validar_cpf():
    cpf=request.form['cpf']
    if calcula_cpf(cpf):
        nome = request.form['nome']
        cursor = db.cursor()
        #define a consulta SQL para inserir o cpf na tabela
        sql = "INSERT INTO PARCEIROS (cpf, nome) values ('"
        sql += cpf + "','" + nome + "');"
        # executa a consulta SQL com o valor do cpf
        cursor.execute(sql)
        # confirma a inserção dos dados no banco de dados
        db.commit() 
        return '<p>CPF válido e processado</p>' +\
                '<p>Para inserir um novo parceiro, clique <a href="http://127.0.0.1:5000/">aqui!</a></p>'
    else:
        return '<p style="color:red">CPF<b>Inválido</b>.</p>' +\
                '<button onclick="history.back()">Voltar</button>'
    
if __name__ == '__main__':
    app.run(debug=True)
