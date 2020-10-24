def encontra_maximo(matriz):
    t=matriz[0]
    maior=t[0]
    for i in range(len(matriz)):
        a=matriz[i]
        for x in range(len(a)):
            if abs(a[x])>abs (a[x-1]):
                if abs(a[x])>maior:
                    maior=abs(a[x])
    return maior