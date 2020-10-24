def calcula_total_da_nota (x,y):
    lista = []
    for i in range (0,len(x)):
        z = x[i] * y[i]
        lista.append (z)
        total = sum(lista)
        return total