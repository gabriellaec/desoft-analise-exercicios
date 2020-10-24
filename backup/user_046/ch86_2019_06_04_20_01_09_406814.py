arquivo=open('dados.csv','r')
arquivo2=open('dados.tsv','w')
conteudo=arquivo.read()
arquivo2.write(conteudo)
arquivo.close()
for d in arquivo2:
    if d==',':
        d.replace('	')
     
    
    
