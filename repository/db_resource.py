import os
import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv
load_dotenv()  

# Inicializa instãncia Banco NoSQL FireStore/Firebase
def firestore_resource():  
    # Obtem credenciais de acesso do firebase
    path_credential = os.environ.get("PATH_CREDENTIAL_FIRESTORE")    
    cred = credentials.Certificate(path_credential)     

    # Verifica se o app padrão já está inicializado
    if not firebase_admin._apps:
        # Se não estiver inicializado, inicialize-o
        firebase_admin.initialize_app(cred)
    else:
        # Se já estiver inicializado, obtem a instância existente
        app = firebase_admin.get_app()

    return firestore.client()