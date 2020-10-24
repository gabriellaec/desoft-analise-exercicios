def inverte_dicionario(dicionario):
    list(dicionario)
    dic_inverte={}
    i=0
    while i < range (len(dicionario)-1):
        dic_inverte[dicionario[i+1]]=dicionario[i]
        i+=1    
    print (dic_inverte)
        