with open ("dados.csv","a") as arquivo1:
    with open ("dados.tsv","a") as arquivo2:
        r=arquivo1.readlines()
        for linhas in r:
            linhas.replace(",","	")  
            arquivo2.write(linhas)

        
        
        
        