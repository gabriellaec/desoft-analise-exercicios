open with ("dados.csv","r")as arquivo:
    conteudo=arquivo.read()
open with("dados.tsv","w")as arquivo:
    arquivo.write(conteudo)