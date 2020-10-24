with open ('churras.txt', 'r') as arquivo:
    dados = arquivo.read() #lê todo o conteúdo em uma única string
    lista_strings = dados.split(',') #separa a string em uma lista de strings a partir do indicador (, )
    iten_qntd ={}
    i=0
    j=1
    while i<len(lista_strings):

        iten_qntd[lista_strings[i]] = lista_strings[j]
        i+=3
        j+=3
    iten_valor ={}
    i=0
    k=2
    while i<len(lista_strings):
        iten_valor[lista_strings[i]] = lista_strings[j]
        i+=3
        k+=3
    valor = 0
    for produto in iten_qntd.keys():
        valor += iten_qntd[produto] * iten_valor[produto]