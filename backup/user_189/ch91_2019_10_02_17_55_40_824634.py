def conta_a():

    
    upper = []
    lista_palavra=[]
    
    contador=0

    with open("palavras.txt","r") as arqv:

        for a in arqv:
            lista_palavra.append(a)
        
        for b in lista_palavra:
            upper.append(b.upper())

        for c in upper:
            split = c.split(" ")
        
                   
        for e in split:
            k = list(e)
            
            if k[0]==" ":
                del k[0]

            elif k[0]=="A":
                contador+=1
                
    return contador

print(conta_a())