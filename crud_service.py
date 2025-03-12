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

def atualizar_livro(Id_Livro, novos_dados):
    db.collection("livros").document(Id_Livro).update(novos_dados)
    print("Livro atualizado!")

def deletar_livro(Id_Livro):
    db.collection("livros").document(Id_Livro).delete()
    print("Livro deletado!")
