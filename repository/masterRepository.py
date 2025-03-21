import repository.db_resource as dbr

# => Main
collection = "masters"              # Nome da coleção de documentos.    <=
db = dbr.firestore_resource()       # Instância de conexão com banco NoSQL

# => Obtem todos os documentos da coleção
def get_all():
    docs_ref = db.collection(collection).order_by("name")  # <==
    docs = docs_ref.stream()    
    return docs

# . localiza um documento a partir de um campo e valor informados
# . response = none ou doc
def find(field: str, value: str):
    response = None
    doc = db.collection(collection).where(field_path=field, op_string="==", value=value).get()
    if doc:
        response = doc        
    return response

# . Exclui um documento
def delete(doc):
    doc[0].reference.delete()

# . Atualiza um documento
def update(doc, new_doc):
    doc[0].reference.update(new_doc)

# . Salva um novo documento
def store(doc):
    doc_ref = db.collection(collection).document()       
    doc_ref.set(doc)   