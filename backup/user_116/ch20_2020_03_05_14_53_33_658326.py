def preco(km):
    if km<=200:
        z=km*0.50
        return (z)
    else:
        y=100+((km-200)*0.45)
        return (y)
km=float(input('quantos km? '))
print("R$ {0:.2f}".format(preco(km)))