def inverte_dicionario(entrada):
    dnovo={}
    for nome, idade in entrada.items():
        if idade not in dnovo.items():
            dnovo[idade]==[]
        dnovo[idade].append(k)
        return dnovo