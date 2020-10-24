arquivo=open('dados.csv','r')
arquivo2=open('dados.tsv','w')
conteudo=arquivo.read()
arquivo2.write(conteudo)
arquivo.close()
arquivo2.close()
    
    
