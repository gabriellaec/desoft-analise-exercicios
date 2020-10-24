ref_arquvio = open("dados.csv","r")
conteudo=ref_arquivo.read()
open with("dados.tsv","w")as arquivo:
    arquivo.write(conteudo)
ref_arquivo.close()