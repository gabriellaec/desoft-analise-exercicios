ref_arquvio = open("dados.csv","r"):
    conteudo=arquivo.read()
open with("dados.tsv","w")as arquivo:
    arquivo.write(conteudo)
ref_arquivo.close()