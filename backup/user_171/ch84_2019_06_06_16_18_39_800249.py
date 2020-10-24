def inverte_dicionario(entrada):
    dnovo={}
    for nome, idade in entrada.items():
        if idade not in dnovo:
            dnovo[idade]=[]
            dnovo[idade].append(nome)    
    return dnovo
