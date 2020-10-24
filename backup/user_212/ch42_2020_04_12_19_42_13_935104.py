lista=[]

palavra=0

while palavra != 'fim':
    palavra=input("Digite uma palavra")
    if palavra[0] == 'a':
        if palavra not in lista:
            lista.append(palavra)
    else:
        lista=lista 
        
print (lista) 
    

    
    
