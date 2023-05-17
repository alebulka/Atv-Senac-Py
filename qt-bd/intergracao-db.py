from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import mysql.connector

banco= mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='',
    database='dbqtdesign'
)

def cadastro():
    exibir=tela.nome.text() and tela.email.text() and tela.telefone.text()
    if exibir == '':
        QMessageBox.about(tela, 'Atenção', 'Preencha os campos solicitados')
    nome = tela.nome.text()
    email = tela.email.text()
    telefone = tela.telefone.text()

    sexo = ''
    if tela.fem.isChecked():
        sexo = 'feminino'
    elif tela.masc.isChecked():
        sexo = 'masculino'
    else:
        sexo = 'não definido'
    cursor= banco.cursor()
    sql="INSET INTO cadastro (nome, email, telefone, sexo) VALUES (%s, %s, %s, %s)"
    colunas = (str(nome), str(email), str(telefone), sexo)
    cursor.execute(sql, colunas)
    banco.commit()

    QMessageBox.about(tela, 'Salvo com sucesso', 'Informações registradas')


app = QtWidgets.QApplication([])
tela = uic.loadUi("tela.ui")
tela.cadastrar.clicked.connect(cadastro)
tela.show()
app.exec()
print('ola')