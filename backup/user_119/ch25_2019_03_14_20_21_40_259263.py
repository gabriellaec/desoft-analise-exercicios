km=int(input("Quantos km? ")
if km>200:
    print(100+(km-200)*0.45)
else:
    print(km*0.5)
print('{0:.2f}'.format(preco(km)))