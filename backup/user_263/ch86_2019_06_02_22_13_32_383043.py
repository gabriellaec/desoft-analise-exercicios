with open('teste.csv','r') as original:
    conteudo = original.read()
    
with open('teste.tsv','w') as final:
    convertido = final.write(conteudo)
    