from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow

import sys

from Servicos.crud_service import adicionar_livro, listar_livros, atualizar_livro, deletar_livro
from Servicos.auth_service import criar_usuario, autenticar_usuario


from telas_SD.Autentificação import *

class Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640, 480)

        self.QtStack = QtWidgets.QStackedLayout()
        
        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()
        self.stack7 = QtWidgets.QMainWindow()
        self.stack8 = QtWidgets.QMainWindow()
        self.stack9 = QtWidgets.QMainWindow()
        self.stack10 = QtWidgets.QMainWindow()
        self.stack11 = QtWidgets.QMainWindow()
        self.stack12 = QtWidgets.QMainWindow()

        # Adiciona os widgets ao layout
        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)
        self.QtStack.addWidget(self.stack7)
        self.QtStack.addWidget(self.stack8)
        self.QtStack.addWidget(self.stack9)
        self.QtStack.addWidget(self.stack10)
        self.QtStack.addWidget(self.stack11)
        self.QtStack.addWidget(self.stack12)

        
        # ENTRA COM AS TELAS AQUI
        self.Autentificação = Ui_Form()
        self.Autentificação.setupUi(self.stack0)
        
class Ui_Main(QMainWindow, Main):
    def __init__(self):
        super(Main, self).__init__(None)
        self.setupUi(self)


