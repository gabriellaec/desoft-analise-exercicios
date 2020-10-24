def inverte_dicionario(dic):
    dicnovo={}
    for nome,idade in dic.itens():
        dicnovo[idade]=nome
        
    return dicnovo
        