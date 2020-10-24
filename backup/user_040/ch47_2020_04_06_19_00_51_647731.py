def estritamente_crescente(x):
    lista = []
    if len(x)>0:
        y = 0
        while y < len(x):
            if x[y]>x[y-1]:
                valor = x[y]
                lista.append(valor)
                y+=1
            else:
                y+=1
        return lista
    else:
        return None