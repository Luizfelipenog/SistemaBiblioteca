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
![Captura de tela 2025-03-14 080908](https://github.com/user-attachments/assets/76fd63c3-4ffa-425a-9ab9-6d7c1c0326c6)
---



