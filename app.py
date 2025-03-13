from Servicos.crud_service import adicionar_livro, listar_livros, atualizar_livro, deletar_livro
from Servicos.auth_service import criar_usuario, autenticar_usuario

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

        # Telas do sistema
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

        self.atual = "tela_inicial" 

        #Aqui vai ficar os botões e a chamada das funções.
        
        #TELA INICIAL
        self.ui.tela_inicial.confirm.clicked.connect(lambda:self.abrirTela('cadastro')())
        self.ui.tela_inicial.confirm_2.clicked.connect(lambda:self.abrirTela('autentificação')())
        
        #TELA LOGIN
        self.ui.autentificação.confirm_4.clicked.connect(self.tela_inicial)
        self.ui.autentificação.confirm_5.clicked.connect(self.autenticar_usuario)
        self.ui.autentificação.traducao_2.returnPressed.connect(lambda: self.ui.autentificação.traducao_3.setFocus())
        self.ui.autentificação.traducao_3.returnPressed.connect(self.autenticar_usuario)

        #TELA CADASTRO
        self.ui.cadastro.confirm_4.clicked.connect(self.tela_inicial)
        self.ui.cadastro.confirm_5.clicked.connect(self.cadastrar_usuario)
        self.ui.cadastro.traducao_2.returnPressed.connect(lambda: self.ui.cadastro.traducao_3.setFocus())
        self.ui.cadastro.traducao_3.returnPressed.connect(self.cadastrar_usuario)
        
        #TELA LIVROS
        self.ui.tela_livros.confirm_4.clicked.connect(self.tela_inicial)
        self.ui.tela_livros.confirm.clicked.connect(lambda:self.abrirTela('tela_adicionar')())
        self.ui.tela_livros.confirm_2.clicked.connect(lambda:self.abrirTela('editar_livros')())
        self.ui.tela_livros.confirm_3.clicked.connect(lambda:self.abrirTela('tela_listar')())
        
        #TELA ADICIONAR
        self.ui.tela_adicionar.confirm_4.clicked.connect(lambda: self.abrirTela("tela_livros")()) 
        self.ui.tela_adicionar.palavra.returnPressed.connect(lambda: self.ui.tela_adicionar.palavra_2.setFocus())       
        self.ui.tela_adicionar.palavra_2.returnPressed.connect(lambda: self.ui.tela_adicionar.traducao_3.setFocus())
        self.ui.tela_adicionar.traducao_3.returnPressed.connect(lambda: self.ui.tela_adicionar.traducao_4.setFocus())
        self.ui.tela_adicionar.traducao_4.returnPressed.connect(self.add)
        
        #TELA EDITAR
        self.ui.editar_livros.confirm_4.clicked.connect(lambda:self.abrirTela("tela_livros")())
        
        #TELA LISTAR
        self.ui.tela_listar.confirm_4.clicked.connect(lambda:self.abrirTela("tela_livros")())
        
    # Funções
    
    def tela_inicial(self):
        if self.atual == "cadastro" or self.atual == "autentificação" or self.atual == "tela_livros":
            self.atual = "tela_inicial"

            self.ui.QtStack.setCurrentWidget(self.ui.telas['tela_inicial'])


    def abrirTela(self, nome_tela):
        if nome_tela == "tela_adicionar":
            self.ui.tela_adicionar.palavra.setText("")
            self.ui.tela_adicionar.palavra_2.setText("")
            self.ui.tela_adicionar.traducao_3.setText("")
            self.ui.tela_adicionar.traducao_4.setText("")

        def mudar_tela():
            self.ui.QtStack.setCurrentWidget(self.ui.telas[nome_tela])
            self.atual = nome_tela

        return mudar_tela
    
    
    # Tela de cadastro
    def cadastrar_usuario(self):
        if self.ui.cadastro.traducao_2.text() == "" or self.ui.cadastro.traducao_3.text() == "":
            QtWidgets.QMessageBox.information(self, 'Erro', 'Digite valores válidos.')
        elif len(self.ui.cadastro.traducao_3.text()) < 6: 
            QtWidgets.QMessageBox.information(self, 'Erro', 'A senha deve ter pelo menos 6 caracteres.')
        else:
            verif = criar_usuario(self.ui.cadastro.traducao_2.text(), self.ui.cadastro.traducao_3.text())
            if verif == None:
                QtWidgets.QMessageBox.information(self, 'Erro', 'Email inválido.')
            else:
                QtWidgets.QMessageBox.information(self, 'Sucesso', 'Usuário cadastrado com sucesso!')
                self.ui.cadastro.traducao_3.setText("")
                self.ui.cadastro.traducao_2.setText("")
                self.tela_inicial()

    #TELA DE LOGIN
        
    def autenticar_usuario(self):
        try:
            email = self.ui.autentificação.traducao_2.text()
            senha = self.ui.autentificação.traducao_3.text()
                        
            if email == '' or senha == '':
                QtWidgets.QMessageBox.information(self, 'Erro', 'Digite valores válidos.')
            else:
                verif = autenticar_usuario(email, senha)
                if verif == None:
                    QtWidgets.QMessageBox.information(self, 'Erro', 'Email ou senha inválidos.')
                else:
                    QtWidgets.QMessageBox.information(self, 'Sucesso', 'Usuário autenticado com sucesso!')
                    self.ui.autentificação.traducao_3.setText("")
                    self.ui.autentificação.traducao_2.setText("")
                    self.atual = "tela_livros"
                    self.ui.QtStack.setCurrentWidget(self.ui.telas['tela_livros'])

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, 'Erro', f'Ocorreu um erro: {e}')
            
    #TELA DE ADICIONAR
    def add(self):
        titulo = self.ui.tela_adicionar.palavra.text()
        autor = self.ui.tela_adicionar.palavra_2.text()
        paginas = self.ui.tela_adicionar.traducao_3.text()
        ano = self.ui.tela_adicionar.traducao_4.text()
        adicionar_livro(titulo,autor,paginas,ano)
        self.ui.tela_adicionar.palavra.setText("")
        self.ui.tela_adicionar.palavra_2.setText("")
        self.ui.tela_adicionar.traducao_3.setText("")
        self.ui.tela_adicionar.traducao_4.setText("")
    
# def adicionar_livro(titulo, autor, paginas, ano

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())
