with open ("churras.txt", "r", encoding="utf-8") as arquivo:
    ler = arquivo.readlines()
    lista = []
    for i in ler:
        c = i.split(",")
        lista.append(c)
    soma = []
    for e in range(0, len(lista)):
        x = lista[e][1]
        y = lista[e][2]
        soma.append(int(x)*float(y))

print (sum(soma))