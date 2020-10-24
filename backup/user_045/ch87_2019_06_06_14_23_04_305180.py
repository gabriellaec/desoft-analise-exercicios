with open('churras.txt','r') as arquivo:
	conteudo = arquivo.read()
    l=conteudo.split(", ")
    c=0
    linha=True
    while linha:
        l=conteudo.split(", ")
        