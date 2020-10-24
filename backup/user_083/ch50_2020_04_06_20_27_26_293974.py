def junta_nome_sobrenome():  
    lista1=['nome1', 'nome2', 'nome3']
    lista2=['oliveira', 'souza', 'silva']
    zipped=zip(lista1,lista2)
    for lista1,lista2 in zipped:
        print('{0} {1}'.format(lista1,lista2))