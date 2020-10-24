def faixa_notas (lista_notas):
    nova_lista=[0]*3
    nova_lista[0]=len(lista_notas)<5
    nova_lista[1]=len(lista_notas)>4 and <8
    nova_lista[2]=len(lista_notas)>7
    return nova_lista