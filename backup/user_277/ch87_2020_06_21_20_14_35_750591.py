with open('churras.txt', 'r') as arquivo:
    dicionario = {}
    lista_conteudo = arquivo.readlines()
    for i in range(len(lista_conteudo)):
        string_inteira = lista_conteudo[i]
        lista_string = string_inteira.split(',')
        dicionario[lista_string[1]] = lista_string[2]
        for j in dicionario.keys():
            dicionario[j][:len(dicionario[j])]
print(dicionario)
        