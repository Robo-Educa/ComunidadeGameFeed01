import pandas as pd
import repository.playerRepository as playerRepository

# => Obtem documentos de uma coleção
def get_docs():    
    df = pd.DataFrame()    
    docs = playerRepository.get_all()
    for doc in docs:
        doc_dict = doc.to_dict()
        formatted_doc = {                   # <=             
            "Nick": doc_dict["nick_name"],            
            "Comunidade": doc_dict["community"],            
            "Avatar": doc_dict["avatar_url"],            
        }               
        df = pd.concat([df, pd.DataFrame([formatted_doc])], ignore_index=True)
    return df

# . Exclui documento a partir de um campo e valor informados
def delete_doc(field, value):
    doc = playerRepository.find(field, value)
    if doc:
        try:        
            playerRepository.delete(doc)
            response = {
                "status": "success",
                "message": "Documento excluído com sucesso."
            } 
        except Exception as e:
            response = {
                "status": "error",
                "message": "Erro ao excluir o documento.",
                "details": str(e)
            }
    else:
        response = {
                "status": "error",
                "message": "Documento não localizado"
            } 

    return response
  
# . Atualiza documento a partir de um campo e valor informados
def update(field, value, new_doc):
    valido, mensagens_erro = validaRequired(new_doc)
    if not valido:
        response = {
            "status": "error",
            "message": "Erro na validação do documento.",
            "details": mensagens_erro
        }
    else:
        doc = playerRepository.find(field, value)
        if doc:
            try:
                playerRepository.update(doc, new_doc)
                response = {
                    "status": "success",
                    "message": "Documento editado com sucesso."
                } 
            except Exception as e:
                response = {
                    "status": "error",
                    "message": "Erro ao editar o documento.",
                    "details": str(e)
                }
        else:
            response = {
                    "status": "error",
                    "message": "Documento não localizado"
                }        
                    
    return response

# => Adiciona documento
def store(doc):
    valido, mensagens_erro = validaRequired(doc)                    # Valida Campos obrigatórios
    if not valido:
        response = {
            "status": "error",
            "message": "Erro na validação do documento.",
            "details": mensagens_erro
        }
    else:    
        valido, mensagens_erro = validaUnique(doc["nick_name"])     # Valida Campos únicos <=
        if not valido:
            response = {
                "status": "error",
                "message": "Erro na validação do documento.", 
                "details": mensagens_erro
            }
        else:        
            try:        
                playerRepository.store(doc)
                response = {
                    "status": "success",
                    "message": "Documento adicionado com sucesso."
                }                                         
            except Exception as e:
                response = {
                    "status": "error",
                    "message": "Erro ao adicionar o documento.",
                    "details": str(e)
                }
    
    return response

# => Valida documento / campos obrigatórios
def validaRequired(doc):
    response = True
    messages = []
    
    if "name" not in doc or not doc["name"]:                # <=
        response = False
        messages.append("O campo 'name' é obrigatório e não pode estar vazio.")
    
    if "nick_name" not in doc or not doc["nick_name"]:      # <=
        response = False
        messages.append("O campo 'nick_name' é obrigatório e não pode estar vazio.")
    
    return response, messages

# => Valida documento / campos de valores únicos
def validaUnique(value):
    status = True
    message = ""

    doc = playerRepository.find("nick_name", value)         # <=
    if doc:
        status = False
        message = "Nick_Name já existe. Escolha outro!"     # <=
    
    return status, message

def get_doc(field, value):
    doc = playerRepository.find(field, value)
    if doc:
        response = doc
    else:
        response = {
                "status": "error",
                "message": "Documento não localizado"
            } 

    return response

    