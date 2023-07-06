from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox

def abre():
    tela.close()
    tela2.show()

def cads():
    if tela2.java.isChecked():
        QMessageBox.about(tela2, 'Atenção', 'Curso java selecionada')
    elif tela2.python.isChecked():
        QMessageBox.about(tela2, 'Atenção', 'Curso python selecionada')
    else:
        QMessageBox.about(tela2, 'Atenção', 'Nenhum curso selecionado!')

def entrar():
    user = tela.inputEmail.text()
    password = tela.inputSenha.text()
    if user == '' or password == '':
        QMessageBox.about(tela, 'Atenção', 'Preencha os campos solicitados!')
    elif user == 'admin' and password == '123':
        QMessageBox.about(tela, ' Usuário OK', 'Usuário Aceito')
        tela.close()
    else:
        QMessageBox.about(tela, 'Atenção', 'Usuário e/ou senha incorretos.')


app = QtWidgets.QApplication([])
tela = app.loadUi("login.ui")
tela2 = app.loadUi("cadastro.ui")
tela.botaoEntrar.clicked.connect(entrar)



tela.show()
app.exec()