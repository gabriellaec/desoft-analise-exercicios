def monta_dicionario(lista1,lsita2):
    dictionary={}
    
    for a in range(len(lista1)):
        dictionary[lista1[a]]= lista2[a]
        
    return dictionary

lista1=["a","b","c","d"]
lista2=[1,2,3,4]

print(monta_dicionario(lista1,lista2))
        
        