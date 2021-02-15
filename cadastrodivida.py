from PyQt5 import uic, QtWidgets
import mysql.connector
from datetime import datetime
from PyQt5.QtWidgets import QMessageBox

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456",
    database="financaspessoais"
)

def selecionartodos():

        cadastrodivida.checkBox.setChecked(True)
        cadastrodivida.checkBox_2.setChecked(True)
        cadastrodivida.checkBox_3.setChecked(True)
        cadastrodivida.checkBox_4.setChecked(True)
        cadastrodivida.checkBox_5.setChecked(True)
        cadastrodivida.checkBox_6.setChecked(True)
        cadastrodivida.checkBox_7.setChecked(True)
        cadastrodivida.checkBox_8.setChecked(True)
        cadastrodivida.checkBox_9.setChecked(True)
        cadastrodivida.checkBox_10.setChecked(True)
        cadastrodivida.checkBox_11.setChecked(True)
        cadastrodivida.checkBox_12.setChecked(True)



def cadastrar():

    cursor = banco.cursor()
    x = cadastrodivida.comboBox.currentText()
    cursor.execute("select id from contabanco where nomebanco = '" + x + "'")
    StrA = cursor.fetchall()
    StrA = (str(StrA).strip('[]'',''()'))
    nome = cadastrodivida.lineEdit.text()
    datatext = cadastrodivida.lineEdit_2.text()
    valor = cadastrodivida.lineEdit_3.text()
    data = str(datetime.strptime(datatext, "%d/%m/%Y").date())



    if (cadastrodivida.checkBox.isChecked()):
        cursor.execute("insert into dividafixa (nome,data, valor, idmes, idconta) values ('" + nome + "','" + data + \
                       "','" + valor + "','" + '1' + "','" + StrA + "')")
        cadastrodivida.checkBox.setChecked(False)

    if (cadastrodivida.checkBox_2.isChecked()):
        cursor.execute("insert into dividafixa (nome,data, valor, idmes, idconta) values ('" + nome + "','" + data + \
                       "','" + valor + "','" + '2' + "','" + StrA + "')")
        cadastrodivida.checkBox_2.setChecked(False)


    if (cadastrodivida.checkBox_3.isChecked()):
        cursor.execute("insert into dividafixa (nome,data, valor, idmes, idconta) values ('" + nome + "','" + data + \
                       "','" + valor + "','" + '3' + "','" + StrA + "')")
        cadastrodivida.checkBox_3.setChecked(False)


    if (cadastrodivida.checkBox_4.isChecked()):
        cursor.execute("insert into dividafixa (nome,data, valor, idmes, idconta) values ('" + nome + "','" + data + \
                       "','" + valor + "','" + '4' + "','" + StrA + "')")
        cadastrodivida.checkBox_4.setChecked(False)


    if (cadastrodivida.checkBox_5.isChecked()):
        cursor.execute("insert into dividafixa (nome,data, valor, idmes, idconta) values ('" + nome + "','" + data +\
                       "','" + valor + "','" + '5' + "','" + StrA + "')")
        cadastrodivida.checkBox_5.setChecked(False)


    if (cadastrodivida.checkBox_6.isChecked()):
        cursor.execute("insert into dividafixa (nome,data, valor, idmes, idconta) values ('" + nome + "','" + data + \
                       "','" + valor + "','" + '6' + "','" + StrA + "')")
        cadastrodivida.checkBox_6.setChecked(False)


    if (cadastrodivida.checkBox_7.isChecked()):
        cursor.execute("insert into dividafixa (nome,data, valor, idmes, idconta) values ('" + nome + "','" + data + \
                       "','" + valor + "','" + '7' + "','" + StrA + "')")
        cadastrodivida.checkBox_7.setChecked(False)


    if (cadastrodivida.checkBox_8.isChecked()):
        cursor.execute("insert into dividafixa (nome,data, valor, idmes, idconta) values ('" + nome + "','" + data + \
                       "','" + valor + "','" + '8' + "','" + StrA + "')")
        cadastrodivida.checkBox_8.setChecked(False)


    if (cadastrodivida.checkBox_9.isChecked()):
        cursor.execute("insert into dividafixa (nome,data, valor, idmes, idconta) values ('" + nome + "','" + data + \
                       "','" + valor + "','" + '9' + "','" + StrA + "')")
        cadastrodivida.checkBox_9.setChecked(False)


    if (cadastrodivida.checkBox_10.isChecked()):
        cursor.execute("insert into dividafixa (nome,data, valor, idmes, idconta) values ('" + nome + "','" + data + \
                       "','" + valor + "','" + '10' + "','" + StrA + "')")
        cadastrodivida.checkBox_10.setChecked(False)


    if (cadastrodivida.checkBox_11.isChecked()):
        cursor.execute("insert into dividafixa (nome,data, valor, idmes, idconta) values ('" + nome + "','" + data + \
                       "','" + valor + "','" + '11' + "','" + StrA + "')")
        cadastrodivida.checkBox_11.setChecked(False)


    if (cadastrodivida.checkBox_12.isChecked()):
        cursor.execute("insert into dividafixa (nome,data, valor, idmes, idconta) values ('" + nome + "','" + data + \
                       "','" + valor + "','" + '12' + "','" + StrA + "')")
        cadastrodivida.checkBox_12.setChecked(False)
        cadastrodivida.checkBox_13.setChecked(False)

    banco.commit()
    # banco.close()

    cadastrodivida.lineEdit.setText("")
    cadastrodivida.lineEdit_2.setText("")
    cadastrodivida.lineEdit_3.setText("")


def execbombobox():
    cursor1 = banco.cursor()
    cursor1.execute("select nomebanco from contabanco")
    bancos = cursor1.fetchall()
    for i in range(len(bancos)):
        bancof = bancos[i][0]
        cadastrodivida.comboBox.addItem(bancof)
        i += 1

def execbombobox2():
    cursor_4 = banco.cursor()
    cursor_4.execute("select nomebanco from contabanco")
    bancos = cursor_4.fetchall()
    for i in range(len(bancos)):
        bancof = bancos[i][0]
        cadastrarc.comboBox.addItem(bancof)
        i += 1


def cadastrob():
    cadastrobanco.show()


def cadastrarbanco():
    cursor3 = banco.cursor()
    nomeb = cadastrobanco.lineEdit.text()
    if (cadastrobanco.radioButton_2.isChecked()):
        debito = "1"
    elif (cadastrobanco.radioButton.isChecked()):
        debito = "0"
    else:
        QMessageBox.about(cadastrobanco,"AVISO","SELECIONE A OPÇÃO PARA O DÉBITO")

    if(cadastrobanco.radioButton_3.isChecked()):
        credito = "1"
    elif(cadastrobanco.radioButton_4.isChecked()):
        credito = "0"
    else:
        QMessageBox.about(cadastrobanco,"AVISO","SELECIONE A OPÇÃO PARA O CRÉDITO (*)")

    limitecredito = cadastrobanco.lineEdit_2.text()

    if(cadastrobanco.radioButton_3.isChecked()):
        cursor3.execute("insert into contabanco (nomebanco, debito, credito, limitecredito) values ('" + nomeb + "','" + \
                        debito + "','" + credito + "','" + limitecredito + "')")
        cadastrobanco.lineEdit.setText("")
        # cadastrobanco.radioButton.setChecked(False)
        # cadastrobanco.radioButton_2.setChecked(False)
        # cadastrobanco.radioButton_3.setChecked(False)
        # cadastrobanco.radioButton_4.setChecked(False)
        cadastrobanco.lineEdit_2.setText("")
        cadastrobanco.label_7.setText("SUCESSO!!!")




    elif(cadastrobanco.radioButton_4.isChecked()):
        cursor3.execute("insert into contabanco (nomebanco, debito, credito, limitecredito) values ('" + nomeb + "','" + \
                        debito + "','" + credito + "', null" + ")")
        cadastrobanco.lineEdit.setText("")
        # cadastrobanco.radioButton.setChecked(False)
        # cadastrobanco.radioButton_2.setChecked(False)
        # cadastrobanco.radioButton_3.setChecked(False)
        # cadastrobanco.radioButton_4.setChecked(False)
        cadastrobanco.lineEdit_2.setText("")
        cadastrobanco.label_7.setText("SUCESSO!!!")


    else:
        print("erro")
    banco.commit()

def painel():
    execbombobox()
    paineldecontrole.close()
    cadastrodivida.show()

def gerenciarbancos():
    listarbancos.show()

    cursor = banco.cursor()
    comandosql = "SELECT nomebanco, debito, credito, limitecredito FROM contabanco "
    cursor.execute(comandosql)
    dadoslidos = cursor.fetchall()

    listarbancos.tableWidget.setRowCount(len(dadoslidos))
    listarbancos.tableWidget.setColumnCount(4)

    for i in range(0,len(dadoslidos)):
        for j in range(0,4):
            if dadoslidos[i][j] == 1:
                celula = "X"
            elif dadoslidos[i][j] == 0 or dadoslidos[i][j] == None:
                celula = "-"
            else:
                celula = dadoslidos[i][j]

            listarbancos.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(celula)))

def excluirbanco():
    cursor = banco.cursor()
    linha = listarbancos.tableWidget.currentRow()

    cursor.execute("select id from contabanco")
    dadoslidos = cursor.fetchall()
    valorid = dadoslidos[linha][0]
    print(valorid)
    cursor.execute("select idconta from dividafixa where idconta = " + str(valorid))
    idcontavinculada = cursor.fetchall()

    if idcontavinculada == []:
        listarbancos.tableWidget.removeRow(linha)
        cursor.execute("delete from contabanco where id = " + str(valorid))
        banco.commit()

    elif int(idcontavinculada[0][0]) == valorid:
        print("Banco está vinculado a movimentações financeiras")


    else:
        print("Ocorreu um erro no comando!")

def showcadastrarcompras():
    cadastrarc.show()
    execbombobox2()


def cadastrarcompras():
    cursor = banco.cursor()
    nomebanco = cadastrarc.comboBox.currentText()
    cursor.execute("select id from contabanco where nomebanco = '" + nomebanco + "'")
    idb = cursor.fetchall()
    idbanco = (str(idb).strip('[]'',''()'))
    descricao = cadastrarc.lineEdit.text()
    data = cadastrarc.lineEdit_2.text()
    data = datetime.strptime(data, "%d/%m/%Y"). date()
    datatex = str(data)
    valor = cadastrarc.lineEdit_3.text()
    parcela01 = cadastrarc.lineEdit_4.text()
    parcela = int(cadastrarc.lineEdit_4.text()) + int(data.month)
    valorparcela = str(int(valor) / int(parcela))
    parcelames = int(data.month)

    # sistema de repetição para percorrer os meses e anos das parcelas divididas a partir da data da compra:
    x = int(data.month) + 1       # começa a contar um mês após o mês da data cadastrada
    y = int(data.year)            # ano da data cadastrada
    while parcelames < parcela:

        cursor.execute("select idano from ano where numeroano = " + str(y))
        idano = cursor.fetchall()
        idano = idano[0][0]
        cursor.execute("select id from mes where numero = " + str(x) + " and  idano = " + str(idano))
        idmes = cursor.fetchall()
        idmes = str(idmes[0][0])

        cursor.execute("insert into cartaofatura (idbanco, produtoservico, data, valor, nparcelas, idmes) values ('" + \
                       idbanco + "','" + descricao + "','" + datatex + "','" + valorparcela + "','" + parcela01 + "','"\
                       + idmes + "')")

        if x < 12:
            x+=1
        else:
            x = x - 11
            y = y + 1
        parcelames += 1
    cadastrarc.lineEdit.setText("")
    cadastrarc.lineEdit_2.setText("")
    cadastrarc.lineEdit_3.setText("")
    cadastrarc.lineEdit_4.setText("")

    banco.commit()


def sair():
    cadastrodivida.comboBox.clear()
    cadastrodivida.close()
    paineldecontrole.show()


def sair_2():
    paineldecontrole.comboBox.clear()
    paineldecontrole.close()


def fecharcadastrobanco():
    cadastrobanco.close()


def fecharcadastrarcompras():
    cadastrarc.comboBox.clear()
    cadastrarc.close()

app = QtWidgets.QApplication([])

cadastrodivida = uic.loadUi("cadastrodivida.ui")
paineldecontrole = uic.loadUi("paineldecontrole.ui")
cadastrobanco = uic.loadUi("cadastrobanco.ui")
listarbancos = uic.loadUi("listarbancos.ui")
cadastrarc = uic.loadUi("cadastarcompras.ui")
paineldecontrole.pushButton_11.clicked.connect(painel)
cadastrodivida.pushButton.clicked.connect(cadastrar)
cadastrodivida.checkBox_13.clicked.connect(selecionartodos)
cadastrodivida.pushButton_2.clicked.connect(sair)
paineldecontrole.pushButton_2.clicked.connect(cadastrob)
paineldecontrole.pushButton_4.clicked.connect(sair_2)
cadastrobanco.pushButton.clicked.connect(cadastrarbanco)
cadastrobanco.pushButton_2.clicked.connect(fecharcadastrobanco)
cadastrobanco.pushButton_3.clicked.connect(gerenciarbancos)
listarbancos.pushButton.clicked.connect(excluirbanco)
paineldecontrole.pushButton_12.clicked.connect(showcadastrarcompras)

cadastrarc.pushButton.clicked.connect(cadastrarcompras)
cadastrarc.pushButton_2.clicked.connect(fecharcadastrarcompras)


paineldecontrole.show()
app.exec()