open with("churras.txt","r")as arquivo:
    conteudo=arquivo.read()
valores=churras.values()
for v in valores:
    print(v)