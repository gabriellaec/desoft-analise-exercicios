def lista_sufixos(string):
    lista=[]
    i=len(string)
    while i< len(string):
        b=string[:i]
        lista.append(b)
        i-=1
    print (lista)
    
        
