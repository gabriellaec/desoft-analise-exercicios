import csv
lista = [] # você só precisa de uma lista - ela é uma matriz multidimensional

with open('macacos-me-mordam.txt', newline='') as csvfile:
    # o nome 'spamreader' abaixo é só exemplo, poderia ser qq. coisa
    spamreader = csv.reader(csvfile, delimiter=',') # separe por vírgula

    # o módulo csv detectará novas linhas automaticamente
    for linha in spamreader:
        lista.append(linha)

# os elementos começam ser contados em zero, i.e. lista[0][1] == 'julian'
print(len(lista)) # imprime a linha 2 da lista, inteira
#print(lista[1][1]) # imprime apenas o segundo item da linha 2