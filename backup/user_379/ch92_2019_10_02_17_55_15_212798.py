dic1={}
dic1={'c':1,'b':1,'d':3}

def simplifica_dict(dicionario):
    lista=[]
    for i in dicionario.keys():
        if i not in lista:
            lista.append(i)
    for i in dicionario.values():
        if i not in lista:
            lista.append(i)
    print(lista)
    return dicionario
        
simplifica_dict(dic1)
