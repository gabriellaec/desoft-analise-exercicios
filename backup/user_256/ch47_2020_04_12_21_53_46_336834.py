def estritamente_crescente(valores):
    i = 1
    t = 0
    nova=[]
    if len(valores)>0:
        nova.append(valores[0])
    else:
        return valores
    while i < len(valores):
        if valores[i] > valores[t]:
            nova.append(valores[i])
            t+=1
        else:
            nova = nova
        i+=1
    return nova
        
        