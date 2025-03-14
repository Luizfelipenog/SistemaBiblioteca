# 📚 Sistema de Biblioteca 

> Este projeto tem como objetivo exercitar conceitos de **Sistemas Distribuídos**, implementando um sistema de **cadastro de livros** utilizando **Python** com interface gráfica e armazenamento no **Firebase**. O sistema é estruturado de forma que **cliente e servidor** estejam separados, garantindo a distribuição das operações.

---

## 🔗 Link do Repositório

[GitHub - Projeto SD](https://github.com/Raileal/Projeto_SD)

---

## 📌 Funcionalidades

✅ **Gerenciamento de livros** (CRUD: Criar, Listar, Atualizar, Excluir)  
✅ **Autenticação de usuários** via **Firebase** (Email/Senha)  
✅ **Interface gráfica interativa** utilizando **PyQt5**  
✅ **Armazenamento no Firebase** (Firestore ou Realtime Database)  
✅ **Mensagens de erro e sucesso** para feedback ao usuário  

---

## ⚙ Tecnologias Utilizadas

- **Python** (Lógica e Backend)
- **PyQt5** (Interface gráfica)
- **Firebase Authentication** (Autenticação de usuários)
- **Firestore ou Realtime Database** (Armazenamento de dados)

---

## 🛠️ Instalação e Configuração

### 🔹 1. Clone o Repositório
```bash
git clone git@github.com:Raileal/Projeto_SD.git
cd Projeto_SD
```

### 🔹 2. Instale as Dependências

Instale:
```bash
pip install PyQt5 firebase-admin
```


### 🔹 3. Execute o Projeto
```bash
python app.py
```

---

## 📂 Estrutura do Projeto

```
📁 Projeto_SD
│-- 📄 app.py  # Arquivo principal da aplicação
│-- 📁 Servicos  # Serviços do sistema
│   │-- 📄 auth_service.py  # Serviço de autenticação
│   │-- 📄 crud_service.py  # Serviço de CRUD
│-- 📁 telas_SD  # Interface gráfica
│   │-- 📄 tela_adicionar.py  # Tela de adição de livros
│   │-- 📄 tela_listar.py  # Tela de listagem de livros
│   │-- 📄 tela_inicial.py  # Tela inicial
│   │-- 📄 tela_livros.py  # Tela de gerenciamento de livros
│   │-- 📄 editar_livros.py  # Tela de edição de livros
│   │-- 📄 cadastro.py  # Tela de cadastro
│   │-- 📄 Autentificação.py  # Tela de autenticação
│-- 📁 BD  # Configuração do banco de dados Firebase
│   │-- 📄 firebase_config.py  # Configuração Firebase
│   │-- 📄 projeto-sd-856ba-firebase-adminsdk-fbsvc-ce5f94f2df.json  # Chave de autenticação Firebase
│-- 📄 README.md  # Documentação do projeto
```

---

## 📸 Capturas de Tela
O sistema feito é simples de se utilizar e facíl de se entender, com as imagens abaixo sendo possível entender seu funcionamento.
![Captura de tela 2025-03-14 143218](https://github.com/user-attachments/assets/fdd6c5bc-ac82-47a7-816d-6e6bfe5cdfda)
Ao abrir o progama no app.py a primeira tela a se vizualizar seria a tela inicial, a qual você pode escolher entre a opção de logar ou cadastrar.
![Captura de tela 2025-03-14 143318](https://github.com/user-attachments/assets/4f272854-b47d-4da3-9794-b98112685d5b)
Escolhendo a opção de cadastrar você sera redirecionado para a tela de cadastro o qual sera necesssario escrever um email e senha validos para o cadastro
e concluir a operação tanto apenas apertando enter ou apertando no botão de confirmar logo abaixo da área de inserção das credencias.
![Captura de tela 2025-03-14 143310](https://github.com/user-attachments/assets/965051f0-e560-4927-9005-e8a41d1667a1)
Com uma conta feita você poderá logar ao sistema o qual da mesma forma do cadastro você pode confirmar apertando o botão de confirmar abaixo ou apenas 
apertando enter.
![Captura de tela 2025-03-14 143437](https://github.com/user-attachments/assets/69a86ca1-c753-4c30-bcb2-6a03123449f9)
Após logar você tera acesso a principal pagina do progama, nela terão 3 opções sendo elas a opção de listar livros, editar livros e adicionar livros.
![Captura de tela 2025-03-14 143518](https://github.com/user-attachments/assets/e96f8c98-31b2-44c0-b968-1f68eab1304f)
Ao clicar na opção de editar livros você sera redirecionado para a tela referente a imagem a cima, nesta tela terá uma lista de todos os livros no 
progama, ao clicar em um item da lista aparecerá nos retangulos azuis os dados daquele item, o qual ao clicar nele e modificar ele você sera capaz
de salvar as alterações feitas apertando no botão de concluir abaixo, caso queira apagar o item apenas é preciso apertar no item na lista e apertar 
o botão de apagar, lembrando que o botão de concluir se é necessário apenas no caso de edição do item na lista, com a operação sendo feita aparecerá
uma mensagem de confirmação caso você queira apagar o item e depois uma mensagem mostrará o resultado da operação e você sera redirecionado para a
pagina principal do progama.
![Captura de tela 2025-03-14 143455](https://github.com/user-attachments/assets/70524689-0f2e-47cd-a664-f19d94612f06)
Ao clicar na opção de listar livros será mostrado uma lista de todos os itens presentes no banco de dados, servido principalmente de comparação e analise
das operaçõe feitas
![Captura de tela 2025-03-14 143446](https://github.com/user-attachments/assets/bb063da7-948c-4162-8b26-dd70dffa5dc0)
E por ultimo na opção de adicionar livros você sera redirecionado para o tela de adicionar o qual ao fornecer os dados do livro ele e apertar enter ou o
botão abaixo será feita a adição do respectivo item no banco de dados, lembrando que pode passar entre as áreas de preenchimento tanto por tab quanto por
enter, ao finalizar a operação uma mensagem aparecerá para anunciar a adição do item.

---



