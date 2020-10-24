arquivo=open("dados.csv",'r')
conteudo=arquivo.read()
conteudo_novo=conteudo.replace("csv","tsv")
arquivo.close()