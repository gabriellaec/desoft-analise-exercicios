with open("churras.txt") as arquivo:
    valor_total=0
    for linha in arquivo:
        lista=linha.split(",")
        valor_total+=lista[1]*lista[2]
print(valor_total)