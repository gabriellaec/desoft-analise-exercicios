with open ('churras.txt', 'r') as arquivo:
    dados = arquivo.readlines()
    lista_strings = dados.split(',')
    iten_qntd ={}
    i=0
    j=1
    while i<len(lista_strings):

        iten_qnd(i) = j
        i+=3
        j+=3
    iten_valor ={}
    i=0
    j=1
    while i<len(lista_strings):
        item_valor(i) = j
        i+=3
        j+=3
    valor = 0
    for iten in iten_qntd.keys:
        valor += iten_qntd.values(iten)*iten_valor.values(iten)