with open('texto.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    lista_conteudo= list(conteudo)
    separado = lista_conteudo.split()
    quant_palavras=0
    for e in separado:
        sem_espaco = e.strip()
        quant_palavras += len(sem_espaco)
    print (quant_palavras)