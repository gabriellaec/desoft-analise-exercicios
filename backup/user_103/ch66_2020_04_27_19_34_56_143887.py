def lista_sufixos(string):
    lista=[]
    i=0
    while i < len(lista):
        a=string[i::1]
        lista.append(a)
        i+=1
        print(lista)
    
        
