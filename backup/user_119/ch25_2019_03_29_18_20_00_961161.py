km=float(input("Quantos km? "))
def preco(km):
    if km>200:
        y=100+(km-200)*0.45
        return y
    else:
        w=km*0.5
        return w
print('{0:.2f}'.format(preco(km)))