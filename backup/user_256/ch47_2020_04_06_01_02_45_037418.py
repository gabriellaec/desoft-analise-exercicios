def estritamente_crescente(valores):
    i = 1
    nova=[]
    while i < len(valores):
        nova.append(valores[0])
        
        while valores[i] > valores[i-1]:
            nova.append(valores[i])
        if valores[i]<= valores[i-1]:
            nova = nova
        i+=1
    return nova
        
        