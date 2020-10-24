with open("churras.txt", 'r') as arquivo:
    valor_total=0
    for linha in arquivo:
        lista=linha.split(",")
        quantidade=int(lista[1])
        preco=int(lista[2])
        valor_total+=quantidade*preco
print(valor_total)