from BD.firebase_config import db
import random

def adicionar_livro(id,titulo, autor, paginas, ano):
    doc_ref = db.collection("livros").add({
        "id": id,
        "titulo": titulo,
        "autor": autor,
        "paginas": paginas,
        "ano": ano
    })
    print(f"Livro adicionado com sucesso! ID do livro: {doc_ref[1].id}")


def listar_livros():
    livros_ref = db.collection("livros").stream()
    livros = {}

    for doc in livros_ref:
        livros[doc.id] = doc.to_dict() 

    return livros





def atualizar_livro(id_livro, novos_dados):
    livros_ref = db.collection("livros").where("id", "==", id_livro).stream()

    livros_encontrados = [livro for livro in livros_ref]

    if not livros_encontrados:
        print(f"Erro: Nenhum livro encontrado com o ID '{id_livro}'")
        return False  

    for livro in livros_encontrados:
        livro.reference.update(novos_dados)
        print(f"Livro com ID '{id_livro}' atualizado com sucesso!")
    
    return True


def deletar_livro(id):
    livros_ref = db.collection("livros").where("id", "==", id).stream()

    livros_encontrados = [livro for livro in livros_ref]

    print("encontrou esse livro: ", livros_encontrados)
    
    if not livros_encontrados:
        print(f"Erro: Nenhum livro encontrado com o ID '{id}'")

    for livro in livros_encontrados:
        livro.reference.delete()
        print(f"Livro com ID '{id}' deletado com sucesso!")
        
        


ids_gerados = set()

def gerar_id_unico():
    while True:

        id_aleatorio = random.randint(1, 10000)
        
        if id_aleatorio not in ids_gerados:
            ids_gerados.add(id_aleatorio) 
            return id_aleatorio

