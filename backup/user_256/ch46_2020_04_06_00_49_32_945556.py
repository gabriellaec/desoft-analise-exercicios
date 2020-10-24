def numero_no_indice(valores):
    i = 0
    nova = []
    while i < len(valores):
        if valores[i]==i:
            nova.append(valores[i])
        if valores[i]!=i:
            nova = nova
        i+=1
    return nova
            