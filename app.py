from Servicos.crud_service import adicionar_livro, listar_livros, atualizar_livro, deletar_livro, gerar_id_unico
from Servicos.auth_service import criar_usuario, autenticar_usuario
import random

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
        self.ui.tela_adicionar.pushButton.clicked.connect(self.add)
        
        #TELA EDITAR
        self.ui.tela_livros.confirm_2.clicked.connect(lambda: (self.carregar_lista_livros(), self.abrirTela('editar_livros')()))
        self.ui.editar_livros.confirm_4.clicked.connect(self.abrirTela("tela_livros"))
        self.ui.editar_livros.lista.itemClicked.connect(self.mostrar_detalhes)
        self.ui.editar_livros.confirm_5.clicked.connect(self.editar_livro)
        self.ui.editar_livros.confirm_6.clicked.connect(self.deletar_livro_selecionado)


        
        #TELA LISTAR
        self.ui.tela_livros.confirm_3.clicked.connect(lambda: (self.exibir_livros(), self.abrirTela('tela_listar')()))
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
            
    def carregar_lista_livros(self):
        self.ui.editar_livros.lista.clear()
        livros = listar_livros()  

        if not livros:
            self.ui.editar_livros.lista.addItem("Nenhum livro encontrado")
            return

        for id_livro, dados in livros.items():
            if dados:
                detalhes = (f"📖 {dados.get('titulo', 'Título Desconhecido')}\n"
                            f"✍️ Autor: {dados.get('autor', 'Desconhecido')}\n"
                            f"📅 Ano: {dados.get('ano', 'Desconhecido')}\n"
                            f"📄 Páginas: {dados.get('paginas', 'Desconhecido')}\n"
                            f"━━━━━━━━━━━━━━━━━━")


                item = QtWidgets.QListWidgetItem(detalhes)


                item.setData(QtCore.Qt.UserRole, dados)

      
                self.ui.editar_livros.lista.addItem(item)
                
                
    def mostrar_detalhes(self, item):
        dados = item.data(QtCore.Qt.UserRole)
        
        if dados:
            titulo = dados.get("titulo", "Título Desconhecido")
            autor = dados.get("autor", "Autor Desconhecido")
            paginas = dados.get("paginas", "Páginas Desconhecidas")
            ano = dados.get("ano", "Ano Desconhecido")


            self.ui.editar_livros.Titulo.setText(titulo)
            self.ui.editar_livros.autor.setText(autor)
            self.ui.editar_livros.paginas.setText(str(paginas))
            self.ui.editar_livros.ano.setText(str(ano))
        else:

            self.ui.editar_livros.Titulo.setText("Desconhecido")
            self.ui.editar_livros.autor.setText("")
            self.ui.editar_livros.paginas.setText("")
            self.ui.editar_livros.ano.setText("")
               
    # Tela Detalhes
    def exibir_livros(self):
        self.ui.tela_listar.lista.clear()  # Limpa a lista antes de adicionar novos itens
        livros = listar_livros()  # Obtém os livros

        if not livros:
            self.ui.tela_listar.lista.addItem("Nenhum livro encontrado")
            return

        # Itera sobre os livros e adiciona os detalhes na lista
        for id_livro, dados in livros.items():
            if isinstance(dados, dict):  # Verifica se dados é um dicionário
                titulo = dados.get('titulo', 'Título Desconhecido')
                autor = dados.get('autor', 'Desconhecido')
                ano = dados.get('ano', 'Desconhecido')
                paginas = dados.get('paginas', 'Desconhecido')

                # Formata os detalhes do livro
                detalhes = (f"📖 {titulo}\n"
                            f"✍️ Autor: {autor}\n"
                            f"📅 Ano: {ano}\n"
                            f"📄 Páginas: {paginas}\n"
                            f"━━━━━━━━━━━━━━━━━━")

                item = QtWidgets.QListWidgetItem(detalhes)  # Cria o item na lista.
                item.setData(QtCore.Qt.UserRole, dados)  # Associa os dados ao item

                self.ui.tela_listar.lista.addItem(item)  # Adiciona o item na lista

    def add(self):
        id = gerar_id_unico()
        titulo = self.ui.tela_adicionar.palavra.text()
        autor = self.ui.tela_adicionar.palavra_2.text()
        paginas = self.ui.tela_adicionar.traducao_3.text()
        ano = self.ui.tela_adicionar.traducao_4.text()
        adicionar_livro(id,titulo,autor,paginas,ano)
        self.ui.tela_adicionar.palavra.setText("")
        self.ui.tela_adicionar.palavra_2.setText("")
        self.ui.tela_adicionar.traducao_3.setText("")
        self.ui.tela_adicionar.traducao_4.setText("")
        
    def editar_livro(self):
        # Obtém os novos dados do formulário
        novo_titulo = self.ui.editar_livros.Titulo.text()
        novo_autor = self.ui.editar_livros.autor.text()
        novo_paginas = self.ui.editar_livros.paginas.text()
        novo_ano = self.ui.editar_livros.ano.text()

        # Obtém o item selecionado na lista
        item_selecionado = self.ui.editar_livros.lista.currentItem()
        if not item_selecionado:
            QtWidgets.QMessageBox.information(self, 'Erro', 'Nenhum livro selecionado.')
            return

        # Extrai os dados associados ao item e obtém o ID do livro
        dados = item_selecionado.data(QtCore.Qt.UserRole)
        if not dados or not isinstance(dados, dict):
            QtWidgets.QMessageBox.information(self, 'Erro', 'Dados do livro inválidos.')
            return

        # Extraia somente o ID
        id_livro = dados.get('id')

        # Cria o dicionário com os dados atualizados
        livro_atualizado = {
            'titulo': novo_titulo,
            'autor': novo_autor,
            'ano': novo_ano,
            'paginas': novo_paginas
        }

        # Chama a função para atualizar o livro usando o ID extraído
        atualizar_livro(id_livro, livro_atualizado)
        QtWidgets.QMessageBox.information(self, 'Ok', 'Atualizou')
        self.abrirTela("tela_livros")()

    def deletar_livro_selecionado(self):
        # Obtém o item selecionado na lista
        item_selecionado = self.ui.editar_livros.lista.currentItem()
        if not item_selecionado:
            QtWidgets.QMessageBox.information(self, 'Erro', 'Nenhum livro selecionado.')
            return

        # Extrai os dados associados ao item e obtém o ID do livro
        dados = item_selecionado.data(QtCore.Qt.UserRole)
        if not dados or not isinstance(dados, dict):
            QtWidgets.QMessageBox.information(self, 'Erro', 'Dados do livro inválidos.')
            return

        id_livro = dados.get('id')

        # Confirmação antes da exclusão
        resposta = QtWidgets.QMessageBox.question(
            self, 'Confirmar Exclusão',
            f'Tem certeza de que deseja excluir "{dados.get("titulo", "Livro Desconhecido")}"?',
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No
        )

        if resposta == QtWidgets.QMessageBox.Yes:
            deletar_livro(id_livro)
            QtWidgets.QMessageBox.information(self, 'Sucesso', 'Livro excluído com sucesso!')
            self.carregar_lista_livros()  # Atualiza a lista após a exclusão



                

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())
