a=input("fale uma palavra")
def palavrascomecadascoma(a):
    lista=[]
    while a !="fim":
        if a[0]== "a":
            lista.append(a)
            a=input("fale uma palavra")
    return lista

lista=palavrascomecadascoma(a)
for e in lista:
    print(lista)
    