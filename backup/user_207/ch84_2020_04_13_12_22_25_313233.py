def inverte_dicionario (dicio_base):
    resposta ={}
    for nome, idade in dicio_base.items():
        
        if idade not in resposta:
            nova_lista =[]
            nova_lista.append (nome)
            resposta[idade] = nova_lista
            
        else:
            nova_lista.append (nome)
            resposta[idade] = nova_lista

    return resposta
