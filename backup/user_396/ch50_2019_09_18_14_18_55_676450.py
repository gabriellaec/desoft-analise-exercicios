def numero_no_indice(z):
    i = 0
    y = []
    while i < len(z):
        if i == z[i]:
            y.append(i)
        i +=1
    return y
    
print(numero_no_indice(z))