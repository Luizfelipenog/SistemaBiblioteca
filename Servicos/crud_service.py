from BD.firebase_config import db

def adicionar_livro(titulo, autor, paginas, ano):
    doc_ref = db.collection("livros").add({
        "titulo": titulo,
        "autor": autor,
        "paginas": paginas,
        "ano": ano
    })
    print(f"Livro adicionado com sucesso! ID do livro: {doc_ref[1].id}")


def listar_livros():
    livros = db.collection("livros").stream()
    for livro in livros:
        print(f"{livro.id} => {livro.to_dict()}")




def atualizar_livro(titulo, novos_dados):
    livros_ref = db.collection("livros").where("titulo", "==", titulo).stream()

    livros_encontrados = [livro for livro in livros_ref]

    if not livros_encontrados:
        print(f"Erro: Nenhum livro encontrado com o título '{titulo}'")
        return

    for livro in livros_encontrados:
        livro.reference.update(novos_dados)
        print(f"Livro '{titulo}' atualizado com sucesso!")


def deletar_livro(id):
    try:
        livro_ref = db.collection("livros").document(id)
        livro = livro_ref.get()

        if livro.exists:
            livro_ref.delete()
            print(f"Livro com ID '{id}' removido com sucesso!")
        else:
            print(f"Erro: Nenhum livro encontrado com o ID '{id}'")

    except Exception as e:
        print(f"Erro ao deletar livro: {e}")
        

