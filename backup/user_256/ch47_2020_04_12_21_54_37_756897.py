def estritamente_crescente(valores):
    nova=[]
    if len(valores)>0:
        nova.append(valores[0])
    else:
        return valores
    i = 1
    t = 0
    while i < len(valores):
        if valores[i] > valores[t]:
            nova.append(valores[i])
            t+=1
        i+=1
    return nova
        
        