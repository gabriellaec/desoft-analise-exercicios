with open('macacos-me-mordam.txt','r') as arquivo:
    linhas=arquivo.readlines()
    lista=[]
    for e in linhas:
        if e=='Banana'or e=='BANANA' or e=='BaNaNa'or e=='banana':
            lista.append(e)
            
         
    print(lista.count())
            
    
    
            