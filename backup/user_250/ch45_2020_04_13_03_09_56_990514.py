z_ou_n = False
lista = []
lista_r = [0]
while z_ou_n == False:
    n = int(input("Digite n: "))
    if n >= 1:
        lista.append(n)
    else:
        z_ou_n = True
        x = (len(lista)-1)
        i = 0
        while x >= 0:
            lista_r[i] = lista[x]
            lista_r.append(lista[x])
            i += 1
            x -= 1
        k = len(lista_r)-1
        del lista_r[k]
        print(lista_r)