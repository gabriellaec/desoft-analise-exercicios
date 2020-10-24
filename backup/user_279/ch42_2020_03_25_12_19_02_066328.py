palavra1 = str(input("digite uma palavra:"))
palavra2 = str(input("digite uma palavra:"))
palavra3 = str(input("digite uma palavra:"))
primeira_letra1 = palavra1[0]
primeira_letra2 = palavra2[0]
primeira_letra3 = palavra3[0]

lista = [palavra1, palavra2, palavra3]
if primeira_letra1 != "a":
    del lista[0]
elif primeira_letra2 != "a":
    del lista[1]
elif primeira_letra3 != "a":
    del lista[2]

print(lista)