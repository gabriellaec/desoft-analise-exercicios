lista = [["janeiro","1"],["fevereiro","2"],["março","3"],["abril","4"],["maio","5"],["junho","6"],["julho","7"],["agosto","8"],["setembro","9"],["outubro","10"],["novembro","11"],["dezembro","12"]]

mes = input("Digite um mes: ")
for i in range(len(lista)):
    if lista[i][0] == mes:
        print("{0}".format(lista[i][1]))