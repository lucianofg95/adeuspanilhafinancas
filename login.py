from PyQt5 import uic, QtWidgets
import mysql.connector

banco=  mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456",
    database="banco_cadastro"
)

def chama_tela_logado():
    primeiratela.label_4.setText("")
    nomeusuario = primeiratela.lineEdit_2.text()
    senha = primeiratela.lineEdit.text()
    cursor = banco.cursor()
    try:
        cursor.execute("SELECT senha FROM cadastro WHERE login = '{}'".format(nomeusuario))
        senhabd = cursor.fetchall()
        banco.close()

    except:
        print("Erro ao validar o login")

    if senhabd[0][0] == senha:
        primeiratela.close()
        logado.show()
    else:
        primeiratela.label_4.setText("Dados de login incorretos!")

def logout():
    logado.close()
    primeiratela.show()

def telecadastro():
    telacadastro.show()

def cadastrar():
    nome = telacadastro.lineEdit.text()
    login = telacadastro.lineEdit_2.text()
    senha = telacadastro.lineEdit_3.text()
    c_senha = telacadastro.lineEdit_4.text()

    if (senha == c_senha):
        try:
            cursor = banco.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS cadastro (nome text,login text,senha text)")
            cursor.execute("INSERT INTO cadastro VALUES ('" + nome + "','" + login + "','" + senha + "')")
            banco.commit()
            banco.close()
            telacadastro.label.setText("Usuario cadastrado com sucesso")
            telacadastro.lineEdit.setText("")
            telacadastro.lineEdit_2.setText("")
            telacadastro.lineEdit_3.setText("")
            telacadastro.lineEdit_4.setText("")

        except mysql.Error as erro:
            print("Erro ao inserir os dados: ", erro)
    else:
        telacadastro.label.setText("As senhas digitadas estão diferentes")



app = QtWidgets.QApplication([])
primeiratela = uic.loadUi("primeiratela.ui")
logado = uic.loadUi("logado.ui")
telacadastro = uic.loadUi("telacadastro.ui")
primeiratela.pushButton.clicked.connect(chama_tela_logado)
logado.pushButton.clicked.connect(logout)
primeiratela.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
primeiratela.pushButton_2.clicked.connect(telecadastro)
telacadastro.pushButton.clicked.connect(cadastrar)


primeiratela.show()
app.exec()