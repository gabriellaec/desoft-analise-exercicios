ref_arquivo = open("churras.txt","r")
conteudo=ref_arquivo.read()
valores=conteudo.values()
for v in valores:
    print(v)