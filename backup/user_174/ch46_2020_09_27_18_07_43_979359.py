def numero_no_indice(valores):
    i=0
    while i<int(valores):
        valores[i]=i
        i=i+1
        return valores[i]
    