dict = {}
dict['felipe']="lacombe"
dict['ohara']="shiba"
def simplifica_dict(dict): 
    dictLista = []
    for key, value in dict.items():
        dictLista = [key,value]
        dictLista.append(dictLista)
    
    print (dictLista)
    for i in dictLista:
        print (i)