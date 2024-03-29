import time

from PyQt5 import uic, QtWidgets
import mysql.connector
from datetime import datetime, date
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDate, Qt

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456",
    database="financaspessoais"
)


def selecionartodos():

        cadastro_despesa.checkBox.setChecked(True)
        cadastro_despesa.checkBox_2.setChecked(True)
        cadastro_despesa.checkBox_3.setChecked(True)
        cadastro_despesa.checkBox_4.setChecked(True)
        cadastro_despesa.checkBox_5.setChecked(True)
        cadastro_despesa.checkBox_6.setChecked(True)
        cadastro_despesa.checkBox_7.setChecked(True)
        cadastro_despesa.checkBox_8.setChecked(True)
        cadastro_despesa.checkBox_9.setChecked(True)
        cadastro_despesa.checkBox_10.setChecked(True)
        cadastro_despesa.checkBox_11.setChecked(True)
        cadastro_despesa.checkBox_12.setChecked(True)


def cadastrar_despesa():
    # Obtenha o cursor usando uma declaração with
    with banco.cursor() as cursor:
        nome_banco = cadastro_despesa.comboBox.currentText()
        cursor.execute("select id from contabanco where nomebanco = %s", (nome_banco,))
        x = cursor.fetchone()[0]
        nome = cadastro_despesa.lineEdit.text()
        data_texto = cadastro_despesa.dateEdit.text()
        valor = cadastro_despesa.lineEdit_3.text()
        data = str(datetime.strptime(data_texto, "%d/%m/%Y").date())
        y = cadastro_despesa.label_Ano.text()
        cursor.execute("select idano from ano where numeroano = %s", (y,))
        idano = cursor.fetchone()[0]

        meses = {
            "1": cadastro_despesa.checkBox,
            "2": cadastro_despesa.checkBox_2,
            "3": cadastro_despesa.checkBox_3,
            "4": cadastro_despesa.checkBox_4,
            "5": cadastro_despesa.checkBox_5,
            "6": cadastro_despesa.checkBox_6,
            "7": cadastro_despesa.checkBox_7,
            "8": cadastro_despesa.checkBox_8,
            "9": cadastro_despesa.checkBox_9,
            "10": cadastro_despesa.checkBox_10,
            "11": cadastro_despesa.checkBox_11,
            "12": cadastro_despesa.checkBox_12,
        }

        for mes_numero, mes_checkbox in meses.items():
            if mes_checkbox.isChecked():
                cursor.execute("select id from mes where numero = %s and idano = %s", (mes_numero, idano))
                idmes = cursor.fetchone()[0]
                cursor.execute("insert into dividafixa (nome, data, valor, idmes, idconta) values (%s, %s, %s, %s, %s)",
                               (nome, data, valor, idmes, x))
            mes_checkbox.setChecked(False)

        banco.commit()
        cadastro_despesa.lineEdit.setText("")
        cadastro_despesa.lineEdit_3.setText("")
        cadastro_despesa.dateEdit.setDate(QDate.currentDate())



def execbombobox():
    cursor1 = banco.cursor()
    cursor1.execute("select nomebanco from contabanco")
    bancos = cursor1.fetchall()
    for i in range(len(bancos)):
        bancof = bancos[i][0]
        cadastro_despesa.comboBox.addItem(bancof)
        i += 1


def execbombobox2():
    cursor_4 = banco.cursor()
    cursor_4.execute("select nomebanco from contabanco")
    bancos = cursor_4.fetchall()
    for i in range(len(bancos)):
        bancof = bancos[i][0]
        cadastrarc.comboBox.addItem(bancof)
        i += 1

def execbombobox3():
    cursor1 = banco.cursor()
    cursor1.execute("select nomebanco from contabanco")
    bancos = cursor1.fetchall()
    for i in range(len(bancos)):
        bancof = bancos[i][0]
        gerenciarcompras.comboBox_3.addItem(bancof)
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
    cadastro_despesa.show()
    cadastro_despesa.label_Ano.setText(paineldecontrole.lineEditAno.text())
    insertYearBD()
    execbombobox()
    cadastro_despesa.dateEdit.setDate(QDate.currentDate())
    cadastro_despesa.lineEdit_3.setText("0")


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

def gerenciar_despesas():
    gerenciardespesas.show()
    cursor = banco.cursor()
    comandosql = "SELECT nome, data, valor FROM dividafixa "
    cursor.execute(comandosql)
    dadoslidos = cursor.fetchall()

    gerenciardespesas.tableWidget.setRowCount(len(dadoslidos))
    gerenciardespesas.tableWidget.setColumnCount(5)

    for i in range(0,len(dadoslidos)):
        for j in range(0,3):
            celula = dadoslidos[i][j]

            gerenciardespesas.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(celula)))

def gerenciar_compras():
    gerenciarcompras.show()
    gerenciarcompras.label_Ano.setText(paineldecontrole.lineEditAno.text())
    cursor = banco.cursor()
    comandosql = "SELECT c.produtoservico,cb.nomebanco as contabanco, c.valor, m.nome as mes, a.numeroano as ano FROM cartaofatura c JOIN mes m ON c.idmes = m.id JOIN ano a ON m.idano = a.idano JOIN contabanco cb on c.idbanco = cb.id"
    cursor.execute(comandosql)
    dadoslidos = cursor.fetchall()
    execbombobox3()
    gerenciarcompras.tableWidget.setRowCount(len(dadoslidos))
    gerenciarcompras.tableWidget.setColumnCount(5)

    for i in range(0,len(dadoslidos)):
        for j in range(0,5):
            celula = dadoslidos[i][j]

            gerenciarcompras.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(celula)))

def filtrar_compras():
    gerenciarcompras.tableWidget.clearContents()
    year = gerenciarcompras.label_Ano.text()
    mes = gerenciarcompras.comboBox_2.currentText()
    contabanco = gerenciarcompras.comboBox_3.currentText()
    cursor = banco.cursor()
    comandosql2 = "SELECT c.produtoservico, cb.nomebanco as contabanco, c.valor, m.nome as mes, a.numeroano as ano FROM cartaofatura c JOIN mes m ON c.idmes = m.id JOIN ano a ON m.idano = a.idano JOIN contabanco cb ON c.idbanco = cb.id WHERE m.nome = '"+ mes + "' AND cb.nomebanco = '" + contabanco + "' AND a.numeroano = '" + year + "'"
    cursor.execute(comandosql2)
    dadoslidos2 = cursor.fetchall()
    gerenciarcompras.tableWidget.setRowCount(len(dadoslidos2))
    gerenciarcompras.tableWidget.setColumnCount(5)

    for i in range(0,len(dadoslidos2)):
        for j in range(0,5):
            celula = dadoslidos2[i][j]
            gerenciarcompras.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(celula)))

    comandosql3 = "SELECT SUM(valor) FROM cartaofatura c JOIN mes m ON c.idmes = m.id JOIN ano a ON m.idano = a.idano JOIN contabanco cb ON c.idbanco = cb.id WHERE m.nome = '"+ mes + "' AND cb.nomebanco = '" + contabanco + "' AND a.numeroano = '" + year + "'"

    cursor.execute(comandosql3)
    dadoslidos3 = cursor.fetchall()
    soma = dadoslidos3[0][0]
    gerenciarcompras.label_3.setText("R$ " + str(soma))

def excluirbanco():
    cursor = banco.cursor()
    linha = listarbancos.tableWidget.currentRow()

    cursor.execute("select id from contabanco")
    dadoslidos = cursor.fetchall()
    valorid = dadoslidos[linha][0]
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

def excluir_despesa():
    cursor = banco.cursor()
    linha = gerenciardespesas.tableWidget.currentRow()

    cursor.execute("select id from dividafixa")
    dadoslidos = cursor.fetchall()
    valorid = dadoslidos[linha][0]
    listarbancos.tableWidget.removeRow(linha)
    cursor.execute("delete from dividafixa where id = " + str(valorid))
    banco.commit()
    gerenciardespesas.tableWidget.removeRow(linha)


def showcadastrarcompras():
    cadastrarc.show()
    cadastrarc.dateEdit.setDate(QDate.currentDate())
    cadastrarc.lineEdit_3.setText("0")
    cadastrarc.lineEdit_4.setText("1")
    cadastrarc.label_Ano.setText(paineldecontrole.lineEditAno.text())
    insertYearBD()
    execbombobox2()


def cadastrarcompras():
    cursor = banco.cursor()
    insertYearBD()
    nomebanco = cadastrarc.comboBox.currentText()
    cursor.execute("select id from contabanco where nomebanco = '" + nomebanco + "'")
    idb = cursor.fetchall()
    idbanco = (str(idb).strip('[]'',''()'))
    descricao = cadastrarc.lineEdit.text()

    data_texto = cadastrarc.dateEdit.text()
    data = datetime.strptime(data_texto, "%d/%m/%Y").date()
    datatex = str(data)
    valor = cadastrarc.lineEdit_3.text()
    parcela01 = cadastrarc.lineEdit_4.text()
    parcela = int(cadastrarc.lineEdit_4.text()) + int(data.month)
    valorparcela = str(int(valor) / int(parcela01))
    parcelames = int(data.month)

    # sistema de repetição para percorrer os meses e anos das parcelas divididas a partir da data da compra:
    x = int(data.month) + 1       # começa a contar um mês após o mês da data cadastrada
    year = cadastrarc.label_Ano.text()        # ano selecionado pelo usuário

    while parcelames < parcela:
        cursor.execute("select idano from ano where numeroano = " + str(year))
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
            year = int(year) + 1

        parcelames += 1

    cadastrarc.lineEdit.setText("")
    cadastrarc.lineEdit_3.setText("")
    cadastrarc.lineEdit_4.setText("")

    banco.commit()


def sair():
    cadastro_despesa.comboBox.clear()
    cadastro_despesa.close()
    paineldecontrole.show()


def sair_2():
    paineldecontrole.comboBox.clear()
    paineldecontrole.close()


def fecharcadastrobanco():
    cadastrobanco.close()


def fecharcadastrarcompras():
    cadastrarc.comboBox.clear()
    cadastrarc.close()


def insertYearBD():
    cursor = banco.cursor()
    year = paineldecontrole.lineEditAno.text()
    cursor.execute("select numeroano from ano where numeroano = " + str(year))
    ano = cursor.fetchall()

    if (ano == []):
        cursor.execute("insert into ano(numeroano) values ('" + year + "')")
        banco.commit()

        cursor.execute("select idano from ano where numeroano = " + str(year))
        idano = cursor.fetchall()
        idano = idano[0][0]

        cursor.execute("insert into mes(nome, numero, idano) values ('janeiro', '1', '" + str(idano) + "'),\
        ('fevereiro', '2', '" + str(idano) + "'),\
        ('março', '3', '" + str(idano) + "'),\
        ('abril', '4', '" + str(idano) + "'),\
        ('maio', '5', '" + str(idano) + "'),\
        ('junho', '6', '" + str(idano) + "'),\
        ('julho', '7', '" + str(idano) + "'),\
        ('agosto', '8', '" + str(idano) + "'),\
        ('setembro', '9', '" + str(idano) + "'),\
        ('outubro', '10', '" + str(idano) + "'),\
        ('novembro', '11', '" + str(idano) + "'),\
        ('dezembro', '12', '" + str(idano) + "')")

        banco.commit()

    else:
        print("Ano já está inserido no banco de dados")

def incrementar_valor(n):
    numero = int(cadastro_despesa.lineEdit_3.text() or "0")
    cadastro_despesa.lineEdit_3.setText(str(numero+n))

def incrementar_valor_compra(n):
    numero = int(cadastrarc.lineEdit_3.text() or "0")
    cadastrarc.lineEdit_3.setText(str(numero+n))

def incrementar_valor_compra_parcelas(n):
    numero = int(cadastrarc.lineEdit_4.text() or "1")
    cadastrarc.lineEdit_4.setText(str(numero+n))

app = QtWidgets.QApplication([])

cadastro_despesa = uic.loadUi("cadastrodivida.ui")
paineldecontrole = uic.loadUi("paineldecontrole.ui")
cadastrobanco = uic.loadUi("cadastrobanco.ui")
listarbancos = uic.loadUi("listarbancos.ui")
cadastrarc = uic.loadUi("cadastarcompras.ui")
gerenciardespesas = uic.loadUi("gerenciardespesas.ui")
gerenciarcompras = uic.loadUi("gerenciarcompras.ui")
paineldecontrole.pushButton_11.clicked.connect(painel)
cadastro_despesa.pushButton.clicked.connect(cadastrar_despesa)
cadastro_despesa.checkBox_13.clicked.connect(selecionartodos)
cadastro_despesa.pushButton_2.clicked.connect(sair)
cadastro_despesa.pushButton_9.clicked.connect(gerenciar_despesas)
cadastrarc.pushButton_9.clicked.connect(gerenciar_compras)
paineldecontrole.pushButton_2.clicked.connect(cadastrob)
paineldecontrole.pushButton_4.clicked.connect(sair_2)
cadastrobanco.pushButton.clicked.connect(cadastrarbanco)
cadastrobanco.pushButton_2.clicked.connect(fecharcadastrobanco)
cadastrobanco.pushButton_3.clicked.connect(gerenciarbancos)
listarbancos.pushButton.clicked.connect(excluirbanco)
gerenciardespesas.pushButton.clicked.connect(excluir_despesa)
paineldecontrole.pushButton_12.clicked.connect(showcadastrarcompras)
gerenciarcompras.pushButton_2.clicked.connect(filtrar_compras)


cadastro_despesa.pushButton_3.clicked.connect(lambda: incrementar_valor(1))
cadastro_despesa.pushButton_4.clicked.connect(lambda: incrementar_valor(10))
cadastro_despesa.pushButton_5.clicked.connect(lambda: incrementar_valor(100))
cadastro_despesa.pushButton_6.clicked.connect(lambda: incrementar_valor(1000))

cadastrarc.pushButton_3.clicked.connect(lambda: incrementar_valor_compra(1))
cadastrarc.pushButton_4.clicked.connect(lambda: incrementar_valor_compra(10))
cadastrarc.pushButton_5.clicked.connect(lambda: incrementar_valor_compra(100))
cadastrarc.pushButton_6.clicked.connect(lambda: incrementar_valor_compra(1000))
cadastrarc.pushButton_7.clicked.connect(lambda: incrementar_valor_compra_parcelas(1))
cadastrarc.pushButton_8.clicked.connect(lambda: incrementar_valor_compra_parcelas(10))

cadastrarc.pushButton.clicked.connect(cadastrarcompras)
cadastrarc.pushButton_2.clicked.connect(fecharcadastrarcompras)


paineldecontrole.show()
today = date.today()
year = today.strftime("%Y")
paineldecontrole.lineEditAno.setText(year)
insertYearBD()

app.exec()




# def insert_year_bd(cursor):
#     ano = cadastrarc.label_Ano.text()
#     cursor.execute("INSERT IGNORE INTO ano (numeroano) VALUES (%s)", (ano,))
#
#
# def obter_id_banco(cursor, nome_banco):
#     cursor.execute("SELECT id FROM contabanco WHERE nomebanco = %s", (nome_banco,))
#     return cursor.fetchone()[0]
#
#
# def obter_id_mes(cursor, numero_mes, ano):
#     cursor.execute("SELECT id FROM mes WHERE numero = %s AND idano = (SELECT idano FROM ano WHERE numeroano = %s)",
#                    (numero_mes, ano))
#     return cursor.fetchone()[0]