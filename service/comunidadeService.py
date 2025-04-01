import pandas as pd
import repository.comunidadeRepository as comunidadeRepository

# => Obtem documentos de uma coleção
def get_docs():    
    df = pd.DataFrame()    
    docs = comunidadeRepository.get_all()
    for doc in docs:
        doc_dict = doc.to_dict()
        formatted_doc = {                   # <=             
            "Comunidade": doc_dict["community"],
            "Cidade": doc_dict["city"],   
            "Latitude": doc_dict["latitude"],
            "Longitude": doc_dict["longitude"],            
        }               
        df = pd.concat([df, pd.DataFrame([formatted_doc])], ignore_index=True)
    return df

# . Exclui documento a partir de um campo e valor informados
def delete_doc(field, value):
    doc = comunidadeRepository.find(field, value)
    if doc:
        try:        
            comunidadeRepository.delete(doc)
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
        doc = comunidadeRepository.find(field, value)
        if doc:
            try:
                comunidadeRepository.update(doc, new_doc)
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
        valido, mensagens_erro = validaUnique(doc["community"])     #  <= Valida Campos únicos
        if not valido:
            response = {
                "status": "error",
                "message": "Erro na validação do documento.", 
                "details": mensagens_erro
            }
        else:        
            try:        
                comunidadeRepository.store(doc)
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
    
    if "community" not in doc or not doc["community"]:                # <=
        response = False
        messages.append("O campo 'Nome da Comunidade' é obrigatório e não pode estar vazio.")    
    
    return response, messages

# => Valida documento / campos de valores únicos
def validaUnique(value):
    status = True
    message = ""

    doc = comunidadeRepository.find("community", value)         # <=
    if doc:
        status = False
        message = "Nome de Comunidade já existe. Informe algum diferencial no nome!"     # <=
    
    return status, message
