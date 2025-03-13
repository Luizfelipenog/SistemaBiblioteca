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
from PyQt5 import QtWidgets, QtCore
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

        #Aqui vai ficar os botões e a chamada das funções.
        
        #TELA INICIAL
        self.ui.tela_inicial.confirm.clicked.connect(self.abrirTela('cadastro'))
        self.ui.tela_inicial.confirm_2.clicked.connect(self.abrirTela('autentificação'))
        
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
        self.ui.tela_livros.confirm.clicked.connect(self.abrirTela('tela_adicionar'))
        self.ui.tela_livros.confirm_2.clicked.connect(self.abrirTela('editar_livros'))
        self.ui.tela_livros.confirm_3.clicked.connect(self.abrirTela('tela_listar'))
        
        #TELA ADICIONAR
        self.ui.tela_adicionar.confirm_4.clicked.connect(self.abrirTela("tela_livros")) 
        self.ui.tela_adicionar.palavra.returnPressed.connect(lambda: self.ui.tela_adicionar.palavra_2.setFocus())       
        self.ui.tela_adicionar.palavra_2.returnPressed.connect(lambda: self.ui.tela_adicionar.traducao_3.setFocus())
        self.ui.tela_adicionar.traducao_3.returnPressed.connect(lambda: self.ui.tela_adicionar.traducao_4.setFocus())
        # self.ui.tela_adicionar.traducao_4.returnPressed.connect()
        
        #TELA EDITAR
        self.ui.tela_livros.confirm_2.clicked.connect(lambda: (self.carregar_lista_livros(), self.abrirTela('editar_livros')()))
        self.ui.editar_livros.confirm_4.clicked.connect(self.abrirTela("tela_livros"))
        # Conectando o clique do item da lista com a função mostrar_detalhes
        self.ui.editar_livros.lista.itemClicked.connect(self.mostrar_detalhes)



        
        #TELA LISTAR
        self.ui.tela_listar.confirm_4.clicked.connect(self.abrirTela("tela_livros"))
        
    # Funções
    
    def tela_inicial(self):
        if self.atual == "cadastro" or self.atual == "autentificação" or self.atual == "tela_livros":
            self.ui.QtStack.setCurrentWidget(self.ui.telas['tela_inicial'])
            self.atual = "tela_inicial"


    def abrirTela(self, nome_tela):
        self.atual = nome_tela
        # Verifica se a tela a ser aberta é 'tela_adicionar' e limpa os campos
        if nome_tela == "tela_adicionar":
            self.ui.tela_adicionar.palavra.setText("")
            self.ui.tela_adicionar.palavra_2.setText("")
            self.ui.tela_adicionar.traducao_3.setText("")
            self.ui.tela_adicionar.traducao_4.setText("")

        # Função interna para mudar a tela
        def mudar_tela():
            self.ui.QtStack.setCurrentWidget(self.ui.telas[nome_tela])

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

        
    def autenticar_usuario(self):
        try:
            email = self.ui.autentificação.traducao_2.text()
            senha = self.ui.autentificação.traducao_3.text()
            
            print(email, senha)
            
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
        
            
    def carregar_lista_livros(self):
        self.ui.editar_livros.lista.clear()  # Limpa a lista antes de adicionar novos itens
        livros = listar_livros()  # Obtém os livros

        if not livros:
            self.ui.editar_livros.lista.addItem("Nenhum livro encontrado")
            return

        for id_livro, dados in livros.items():
            if dados:
                # Formata os detalhes do livro em um bloco de texto
                detalhes = (f"📖 {dados.get('titulo', 'Título Desconhecido')}\n"
                            f"✍️ Autor: {dados.get('autor', 'Desconhecido')}\n"
                            f"📅 Ano: {dados.get('ano', 'Desconhecido')}\n"
                            f"📄 Páginas: {dados.get('paginas', 'Desconhecido')}\n"
                            f"━━━━━━━━━━━━━━━━━━")

                # Cria o item na lista
                item = QtWidgets.QListWidgetItem(detalhes)

                # Associa os dados completos do livro ao item para futura recuperação
                item.setData(QtCore.Qt.UserRole, dados)

                # Adiciona o item à lista
                self.ui.editar_livros.lista.addItem(item)
                
                
    def mostrar_detalhes(self, item):
        # Obtém os dados do item clicado (ID do livro associado ao item)
        dados = item.data(QtCore.Qt.UserRole)
        
        if dados:
            titulo = dados.get("titulo", "Título Desconhecido")
            autor = dados.get("autor", "Autor Desconhecido")
            paginas = dados.get("paginas", "Páginas Desconhecidas")
            ano = dados.get("ano", "Ano Desconhecido")

            # Atualiza os labels com as informações do livro clicado
            self.ui.editar_livros.informacoes.setText(titulo)
            self.ui.editar_livros.informacoes_2.setText(autor)
            self.ui.editar_livros.informacoes_3.setText(str(paginas))
            self.ui.editar_livros.informacoes_4.setText(str(ano))
        else:
            # Caso não encontre os dados
            self.ui.editar_livros.informacoes.setText("Desconhecido")
            self.ui.editar_livros.informacoes_2.setText("")
            self.ui.editar_livros.informacoes_3.setText("")
            self.ui.editar_livros.informacoes_4.setText("")





    

                
                

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())
