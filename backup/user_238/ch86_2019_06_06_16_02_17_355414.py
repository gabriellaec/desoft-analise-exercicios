with open ("dados.csv","a") as arquivo:
    r=arquivo.readlines()
    for linhas in r:
        linhas.replace(",","	")
        
        with open ("dados.tsv","w") as arquivo2:
            arquivo2.write(linhas)

        
        
        
        