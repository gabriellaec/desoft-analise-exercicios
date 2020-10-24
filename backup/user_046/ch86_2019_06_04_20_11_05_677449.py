with open('dados.csv','r') as arquivo:
with open('dados.tsv','w') as arquivo2:
    conteudo = arquivo.read()
    i=0
    while i < len(conteudo):
        if conteudo[i] == ',':
            conteudo[i] == '    '
        i+=1
    arquivo2.write(conteudo)
     
   
    
