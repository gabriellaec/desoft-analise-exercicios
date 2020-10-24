def aniversariantes_de_setembro(dicionario):
    for i in range(len(dicionario)):
        quero=dicionario['setembro']
        if dicionário[i]!=quero:
            i+=1
        else:
            return quero.values
            