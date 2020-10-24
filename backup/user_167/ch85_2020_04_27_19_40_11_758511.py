with open ('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo=arquivo.readlines()
    
    
    cont=0
    for e in conteudo:
        for palavra in e.split():
            if palavra.lower()=='banana':
                cont+=1
    print(cont)
    
   
        
    

            