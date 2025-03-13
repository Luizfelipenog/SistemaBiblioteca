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

Crie um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
```

Instale as dependências:
```bash
pip install -r requirements.txt
```

Caso o arquivo `requirements.txt` não esteja presente, instale manualmente:
```bash
pip install PyQt5 firebase-admin
```

### 🔹 3. Configuração do Firebase

1. Crie um projeto no [Firebase](https://firebase.google.com/)
2. Ative **Firestore** ou **Realtime Database**
3. Ative **Authentication (Email/Senha)**
4. Baixe o arquivo `firebase-config.json` e coloque na raiz do projeto

### 🔹 4. Execute o Projeto
```bash
python app.py
```

---

## 📂 Estrutura do Projeto

```
📁 Projeto_SD
│-- 📄 app.py  # Arquivo principal da aplicação
│-- 📄 firebase_config.py  # Configuração do Firebase
│-- 📁 Servicos  # Serviços da aplicação
│   │-- 📄 crud_service.py  # CRUD de livros
│   │-- 📄 auth_service.py  # Serviço de autenticação
│-- 📁 telas_SD  # Interface gráfica
│   │-- 📄 Autentificacao.py  # Tela de login
│   │-- 📄 cadastro.py  # Tela de cadastro de usuário
│   │-- 📄 editar_livros.py  # Tela de edição de livros
│   │-- 📄 tela_adicionar.py  # Tela de adição de livros
│   │-- 📄 tela_inicial.py  # Tela inicial
│   │-- 📄 tela_listar.py  # Tela de listagem de livros
│   │-- 📄 tela_livros.py  # Tela de gerenciamento de livros
│-- 📄 requirements.txt  # Dependências do projeto
│-- 📄 README.md  # Documentação do projeto
```

---

## 📸 Capturas de Tela
(Adicione aqui prints da interface gráfica)

---

## 📝 Contribuição
Se quiser contribuir com melhorias, siga os passos:

1. **Fork** o repositório
2. Crie uma branch para suas alterações: `git checkout -b minha-feature`
3. Commit suas alterações: `git commit -m 'Minha nova feature'`
4. Push para o repositório: `git push origin minha-feature`
5. Abra um **Pull Request**

---

## 📄 Licença
Este projeto está sob a licença **MIT**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Se precisar de ajustes ou algo mais, me avise! 🚀
