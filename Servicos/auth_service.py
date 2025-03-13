from firebase_admin import auth
import pyrebase

def criar_usuario(email, senha):
    try:
        user = auth.create_user(email=email, password=senha)
        print(f"Usuário criado com sucesso: {user.uid}")
        if user:
            print("Usuário autenticado com sucesso!")
            return user
        else:
            print("Email ou senha inválidos!")
            return None
    except Exception as e:
        print(f"Erro ao criar usuário: {e}")
        return None

def autenticar_usuario(email, senha):
    
    config = {
        "apiKey": "AIzaSyCnoNPq6vBJ70C4XH3azPFYXbnCIX-PoWc",
        "authDomain": "projeto-sd-856ba.firebaseapp.com",
        "databaseURL": "https://projeto-sd-856ba-default-rtdb.firebaseio.com/",
        "storageBucket": "projeto-sd-856ba.firebasestorage.app"
    }
    
    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()
    
    try:
        user = auth.sign_in_with_email_and_password(email, senha)
        print("Usuário autenticado com sucesso!")
        if user:
            print("Usuário autenticado com sucesso!")
            return user
        else:
            print("Email ou senha inválidos!")
            return None
    except Exception as e:
        print("Erro na autenticação:", e)
        return None

