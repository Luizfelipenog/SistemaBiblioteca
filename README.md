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
![Captura de tela 2025-03-14 080908](https://github.com/user-attachments/assets/76fd63c3-4ffa-425a-9ab9-6d7c1c0326c6)
Ao abrir o progama no app.py a primeira tela a se vizualizar seria a tela inicial, a qual você pode escolher entre a opção de logar ou cadastrar.
![Captura de tela 2025-03-14 080915](https://github.com/user-attachments/assets/75d4ba10-c8c1-44d5-8340-f1d81e175330)
escolhendo a opção de cadastrar você sera redirecionado para a tela de cadastro o qual sera necesssario escrever um email e senha validos para o cadastro
e concluir a operação tanto apenas apertando enter ou apertando no botão de confirmar logo abaixo da área de inserção das credencias.
![Captura de tela 2025-03-14 080933](https://github.com/user-attachments/assets/afc5a41a-ce95-4ad7-9793-a5aa5771be94)
Com uma conta feita você poderá logar ao sistema o qual da mesma forma do cadastro você pode confirmar apertando o botão de confirmar abaixo ou apenas 
apertando enter.
![Captura de tela 2025-03-14 081005](https://github.com/user-attachments/assets/26d69ba4-a78c-4327-9b29-5e24a36ef813)
![Captura de tela 2025-03-14 141725](https://github.com/user-attachments/assets/63809922-fe0c-4a0c-a2c3-ef1b9316d434)
![Captura de tela 2025-03-14 141737](https://github.com/user-attachments/assets/34c0fbaa-0979-49ed-8f86-73ce8914152e)
---



