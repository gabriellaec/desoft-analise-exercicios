with open('texto.txt', 'r') as arquivo:
    conteudo_completo = arquivo.read()
    conteudo_sem_espaco = conteudo_completo.split()
    qntd_palavras = len(conteudo_sem_espaco)
    print(qntd_palavras)