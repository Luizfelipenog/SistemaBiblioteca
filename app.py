from crud_service import adicionar_livro, listar_livros, atualizar_livro, deletar_livro
from auth_service import criar_usuario, autenticar_usuario

def main():
    while True:
        print("\nMenu:")
        print("1. Adicionar Livro")
        print("2. Listar Livros")
        print("3. Atualizar Livro")
        print("4. Deletar Livro")
        print("5. Criar Usuario")
        print("6. Autenticar Usuaio")
        print("0. Sair")
        
        escolha = input("Escolha uma opcao: ")
        
        if escolha == "1":
            id = input("ID do Livro: ")
            titulo = input("Título: ")
            autor = input("Autor: ")
            paginas = int(input("Páginas: "))
            ano = int(input("Ano: "))
            adicionar_livro(id,titulo, autor, paginas, ano)
        elif escolha == "2":
            listar_livros()
        elif escolha == "3":
            titulo = input("Título do Livro: ")
            novos_dados = {}
            novo_titulo = input("Novo Título (deixe em branco para não alterar): ")
            if novo_titulo:
                novos_dados["titulo"] = novo_titulo
            autor = input("Novo Autor (deixe em branco para não alterar): ")
            if autor:
                novos_dados["autor"] = autor
            paginas = input("Novas Páginas (deixe em branco para não alterar): ")
            if paginas:
                novos_dados["paginas"] = int(paginas)
            ano = input("Novo Ano (deixe em branco para não alterar): ")
            if ano:
                novos_dados["ano"] = int(ano)
            atualizar_livro(titulo, novos_dados)
        # elif escolha == "4":
        #     id_livro = input("ID do Livro: ")
        #     deletar_livro(id_livro)
        elif escolha == "4":
         titulo = input("Título do Livro a ser removido: ")
         deletar_livro(titulo)

        elif escolha == "5":
            email = input("Email: ")
            senha = input("Senha: ")
            criar_usuario(email, senha)
        elif escolha == "6":
            email = input("Email: ")
            senha = input("Senha: ")
            autenticar_usuario(email, senha)
        elif escolha == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
