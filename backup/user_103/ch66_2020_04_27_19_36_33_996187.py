def lista_sufixos(string):
    lista=[]
    i=0
    while i < len(string)-1:
        a=string[i::1]
        lista.append(a)
        i+=1
        print(lista)
    
        
