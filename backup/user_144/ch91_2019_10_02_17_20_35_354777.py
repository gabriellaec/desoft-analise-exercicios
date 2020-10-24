with open("palavras.txt","r",encoding = "utf8") as arquivo:
    conteudo = arquivo.read()  
    conteudo = conteudo.lower()    
    split = conteudo.split()
    
    i = 0
    for palavra in range(len(split)):
        palavra = split[i]
        if palavra[0] == "a":
            i+=1
    print(i)
    
    
    