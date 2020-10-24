def verifica_primos(listanumint):
    dicionario=dict()
    i=0
    while i<len(listanumint):
        num = eh_primo(listanumint[i])
        if num==True:
            dicionario[listanumunt[i]]==True
        else:
            dicionario[listanumint[i]]==False
    return dicionario
        