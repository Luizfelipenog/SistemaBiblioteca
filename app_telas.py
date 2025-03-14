import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from telas_SD.Autentificação import autentificação  
from telas_SD.cadastro import cadastro  
from telas_SD.editar_livros import editar_livros  
from telas_SD.tela_adicionar import tela_adicionar  
from telas_SD.tela_inicial import tela_inicial  
from telas_SD.tela_listar import tela_listar  
from telas_SD.tela_livros import tela_livros  


class Ui_Main:
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640, 480)
        
        self.QtStack = QtWidgets.QStackedLayout()
        
        self.telas = {
            'tela_inicial': QtWidgets.QWidget(),
            'autentificação': QtWidgets.QWidget(),
            'cadastro': QtWidgets.QWidget(),
            'editar_livros': QtWidgets.QWidget(),
            'tela_adicionar': QtWidgets.QWidget(),
            'tela_listar': QtWidgets.QWidget(),
            'tela_livros': QtWidgets.QWidget(),
        }        
    
        self.tela_inicial = tela_inicial()
        self.tela_inicial.setupUi(self.telas['tela_inicial'])
        
        self.autentificação = autentificação()
        self.autentificação.setupUi(self.telas['autentificação'])

        self.cadastro = cadastro()
        self.cadastro.setupUi(self.telas['cadastro'])
        
        self.editar_livros = editar_livros()
        self.editar_livros.setupUi(self.telas['editar_livros'])
        
        self.tela_adicionar = tela_adicionar()
        self.tela_adicionar.setupUi(self.telas['tela_adicionar'])
                
        self.tela_listar = tela_listar()
        self.tela_listar.setupUi(self.telas['tela_listar'])

        self.tela_livros = tela_livros()
        self.tela_livros.setupUi(self.telas['tela_livros'])
        
        for tela in self.telas.values():
            self.QtStack.addWidget(tela)

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__(None)
        
        self.ui = Ui_Main()
        self.ui.setupUi(self)

    
    #Aqui vai ficar os botões e a chamada das funções.
    
        #TELA INICIAL
        self.ui.tela_inicial.confirm.clicked.connect(self.abrirTela('cadastro'))
        self.ui.tela_inicial.confirm_2.clicked.connect(self.abrirTela('autentificação'))
        
        #TELA LOGIN
        self.ui.autentificação.confirm_4.clicked.connect(self.retornar)
        #TELA CADASTRO
        self.ui.cadastro.confirm_4.clicked.connect(self.retornar)
        
        
    def retornar(self):
        if self.atual == "cadastro" or self.atual == "autentificação":
            self.ui.QtStack.setCurrentWidget(self.ui.telas['tela_inicial'])
            self.atual = "tela_inicial"



    def abrirTela(self, nome_tela):
        def mudar_tela():
            self.atual = nome_tela
            self.ui.QtStack.setCurrentWidget(self.ui.telas[nome_tela])
        return mudar_tela
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())
