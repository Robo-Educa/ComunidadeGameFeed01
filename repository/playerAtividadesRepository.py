import repository.db_resource as dbr

# => Main
collection = "players_atividades"   # Nome da coleção de documentos.    <=
db = dbr.firestore_resource()       # Instância de conexão com banco NoSQL

def get_all():
    docs = db.collection(collection).stream()    
    return docs