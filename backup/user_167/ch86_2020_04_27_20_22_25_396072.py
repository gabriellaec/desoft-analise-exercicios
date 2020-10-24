import json
with open ('dados.csv','r') as arquivo:
    conteudo=arquivo.read()
    palavras=''
    for e in arquivo:
        if e == ',':
            palavras+="\t"
        else:
            palavras+=e
    with open ('dados.tsv','w') as arquivo2:
        arquivo2.write(palavras)
        
      
        
   
    