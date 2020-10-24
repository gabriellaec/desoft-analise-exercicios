'''with open('churras.txt', 'r', encoding="utf8") as arquivo:
        lista = []
        valor  =  0
        quantidade = []
        preço = []
        conteudo = arquivo.readlines()
        for i in conteudo:
                lista.append(i.split(','))

        for i in lista:
                quantidade.append(i[1])
                preço.append(i[2])
        
        for i in range(0,len(quantidade)):
                valor += float(quantidade[i]) * float(preço[i])
        print(valor)
'''

with open('churras.txt', 'r',  encoding="utf8") as custo_churrasco:
    #lista em que são transcripitados os itens da tabela
    lista = []
    #dicionario que salva o total de cada item 
    dicionario_churrasco = {}
    #separa todas as linhas em uma só lista
    lista_churrasco = custo_churrasco.readlines()
    #cria uma lista individual para cada linha
    for linha in lista_churrasco:
        lista.append(linha.split(','))
    #calcula o valor dado para cada item e salva no dicionario
    for mini_lista in lista:
        dicionario_churrasco[mini_lista[0]] = float(mini_lista[1]) * float(mini_lista[2])

    total = 0
    for item in dicionario_churrasco:
        total += dicionario_churrasco[item]
print(total)
