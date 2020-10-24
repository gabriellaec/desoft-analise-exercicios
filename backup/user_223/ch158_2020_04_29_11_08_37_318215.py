with open('texto.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    separado = conteudo.split()
    quant_palavras=0
    for e in separado:
        quant_palavras += len(e)
    print (quant_palavras)