def preco(km):
    if km>200:
        return 100+(km-200)*0.45
    else:
        return km*0.5
    km=int(input("Quantos km? ")
print('{0:.2f}'.format(preco(km)))