lista1=['lucas', 'guilherme', 'rodrigo']
lista2=['oliveira', 'souza', 'silva']
zipped=zip(lista1,lista2)
def junta_nome_sobrenome(x):
    for lista1,lista2 in zipped:
        print('{0} {1}'.format(lista1,lista2))