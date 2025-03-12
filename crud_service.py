from firebase_config import db

def adicionar_livro(Id_Livro, titulo, autor, paginas, ano):
    db.collection("livros").add({
        "Id_Livro": Id_Livro,
        "titulo": titulo,
        "autor": autor,
        "paginas": paginas,
        "ano": ano
    })
    print("Livro adicionado com sucesso!")

def listar_livros():
    livros = db.collection("livros").stream()
    for livro in livros:
        print(f"{livro.id} => {livro.to_dict()}")



# def atualizar_livro(id_livro, novos_dados):
#     livro_ref = db.collection("livros").document(id_livro)
#     livro = livro_ref.get()

#     if livro.exists:
#         livro_ref.update(novos_dados)
#         print(f"Livro {id_livro} atualizado com sucesso!")
#     else:
#         print(f"Erro: Livro com ID {id_livro} não encontrado!")




def atualizar_livro(titulo, novos_dados):
    livros_ref = db.collection("livros").where("titulo", "==", titulo).stream()

    livros_encontrados = [livro for livro in livros_ref]

    if not livros_encontrados:
        print(f"Erro: Nenhum livro encontrado com o título '{titulo}'")
        return

    for livro in livros_encontrados:
        livro.reference.update(novos_dados)
        print(f"Livro '{titulo}' atualizado com sucesso!")



# def deletar_livro(Id_Livro):
#     db.collection("livros").document(Id_Livro).delete()
#     print("Livro deletado!")


def deletar_livro(titulo):
    livros_ref = db.collection("livros").where("titulo", "==", titulo).stream()

    livros_encontrados = [livro for livro in livros_ref]

    if not livros_encontrados:
        print(f"Erro: Nenhum livro encontrado com o título '{titulo}'")
        return

    for livro in livros_encontrados:
        livro.reference.delete()
        print(f"Livro '{titulo}' removido com sucesso!")
