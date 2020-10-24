def estritamente_crescente(listan):
    nova = []
    i = 0
    while listan[i]<listan[1+i]:
        nova.append(listan[i])
        i += 1
    return nova
        
        