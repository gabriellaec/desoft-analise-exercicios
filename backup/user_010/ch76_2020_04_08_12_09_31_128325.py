def aniversariantes_de_setembro (dic):
    setembro={}
    for chave,valor in dic.items():
        listadata=valor.split("/")
        if listadata[1]=="09":
            setembro[chave]=valor
    return setembro