from Servicos.crud_service import adicionar_livro, listar_livros, atualizar_livro, deletar_livro
from Servicos.auth_service import criar_usuario, autenticar_usuario

# def main():
#     while True:
#         print("\nMenu:")
#         print("1. Adicionar Livro")
#         print("2. Listar Livros")
#         print("3. Atualizar Livro")
#         print("4. Deletar Livro")
#         print("5. Criar Usuario")
#         print("6. Autenticar Usuaio")
#         print("0. Sair")
        
#         escolha = input("Escolha uma opcao: ")
        
#         if escolha == "1":
#             titulo = input("Título: ")
#             autor = input("Autor: ")
#             paginas = int(input("Páginas: "))
#             ano = int(input("Ano: "))
#             adicionar_livro(titulo, autor, paginas, ano)
#         elif escolha == "2":
#             listar_livros()
#         elif escolha == "3":
#             titulo = input("Título do Livro: ")
#             novos_dados = {}
#             novo_titulo = input("Novo Título (deixe em branco para não alterar): ")
#             if novo_titulo:
#                 novos_dados["titulo"] = novo_titulo
#             autor = input("Novo Autor (deixe em branco para não alterar): ")
#             if autor:
#                 novos_dados["autor"] = autor
#             paginas = input("Novas Páginas (deixe em branco para não alterar): ")
#             if paginas:
#                 novos_dados["paginas"] = int(paginas)
#             ano = input("Novo Ano (deixe em branco para não alterar): ")
#             if ano:
#                 novos_dados["ano"] = int(ano)
#             atualizar_livro(titulo, novos_dados)

#         elif escolha == "4":
#          titulo = input("Título do Livro a ser removido: ")
#          deletar_livro(titulo)

#         elif escolha == "5":
#             email = input("Email: ")
#             senha = input("Senha: ")
#             criar_usuario(email, senha)
#         elif escolha == "6":
#             email = input("Email: ")
#             senha = input("Senha: ")
#             autenticar_usuario(email, senha)
#         elif escolha == "0":
#             break
#         else:
#             print("Opção inválida. Tente novamente.")

# if __name__ == "__main__":
#     main()

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
