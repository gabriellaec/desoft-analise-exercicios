with open("texto.txt","r") as arquivo:
    lista = arquivo.split()
    soma = 0
    for e in lista:
        soma += 1
    return soma