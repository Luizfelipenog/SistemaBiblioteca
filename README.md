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
📸 Capturas de Tela
O sistema é simples de utilizar e fácil de entender. As imagens abaixo ilustram seu funcionamento.

🏠 Tela Inicial

![Captura de tela 2025-03-14 143218](https://github.com/user-attachments/assets/1bb68504-862e-424a-913f-cc2408f84547)


Ao abrir o programa no app.py, a primeira tela exibida será a tela inicial, onde você pode escolher entre as opções "Logar" ou "Cadastrar".

📝 Tela de Cadastro

![Captura de tela 2025-03-14 143318](https://github.com/user-attachments/assets/759121d7-7a5b-4da7-b339-97630d2ba76b)


Se escolher "Cadastrar", será redirecionado para a tela de cadastro. Basta inserir um e-mail e uma senha válidos para criar uma conta.
A operação pode ser concluída pressionando Enter ou clicando no botão "Cadastrar" abaixo da área de inserção das credenciais.

🔑 Tela de Login

![Captura de tela 2025-03-14 143310](https://github.com/user-attachments/assets/a77bdd1c-b27b-4e15-b39e-22fcb7425bdc)


Com a conta criada, você pode realizar o login da mesma forma que o cadastro, confirmando com Enter ou clicando no botão "Entrar".

📚 Tela Principal

![Captura de tela 2025-03-14 143437](https://github.com/user-attachments/assets/66398e6a-a6ae-4380-a8f9-2f3a2a0a98e2)


Após o login, você terá acesso à tela principal do programa, que oferece três opções:
✅ Listar Livros
✏️ Editar Livros
➕ Adicionar Livros

✏️ Editar Livros

![Captura de tela 2025-03-14 143518](https://github.com/user-attachments/assets/98e19320-d7d5-4c0a-be7b-99e78d5a680f)


Na tela de edição, será exibida uma lista de todos os livros cadastrados. Ao selecionar um item da lista, seus detalhes aparecerão nos campos azuis.

Para editar, basta modificar os campos e clicar em "Concluir" para salvar as alterações.
Para apagar, selecione o item e clique no botão "Apagar". Uma mensagem de confirmação será exibida antes da exclusão.

📋 Listar Livros

![Captura de tela 2025-03-14 143455](https://github.com/user-attachments/assets/6145c793-31d0-4aa8-8c7b-8f96dcceac02)


A opção "Listar Livros" exibe todos os itens cadastrados no banco de dados, facilitando a análise e comparação de informações.

➕ Adicionar Livros

![Captura de tela 2025-03-14 143446](https://github.com/user-attachments/assets/9d8a1cde-4cee-4afc-a942-1d1c4efae13c)


Na tela de adição, basta inserir os detalhes do livro e pressionar Enter ou clicar no botão "Adicionar livro".

É possível navegar entre os campos pressionando Tab ou Enter.
Após a adição do item, uma mensagem confirmará o sucesso da operação.

---



