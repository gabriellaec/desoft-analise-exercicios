with open('dados.csv','r') as original:
    conteudo = original.read()
    
with open('dados.tsv','w') as final:
    convertido = final.write(conteudo)
    