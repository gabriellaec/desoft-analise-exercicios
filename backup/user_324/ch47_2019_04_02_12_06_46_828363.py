lista = [["1", "janeiro"], ["2", "fevereiro"],["3", "março"]]
nome = input("Digite um nome? ")
for i in range(len(lista)):
    if lista[i][0] == nome:
        print("Telefone: {0}".format(lista[i][1]))