with open("dados.csv", "r") as arquivo:
    conteudo = arquivo.read()
with open("dados.tlv", "a") as arquivo2:
    b= conteudo.replace(",","\t")
    l = arquivo2.write(b)