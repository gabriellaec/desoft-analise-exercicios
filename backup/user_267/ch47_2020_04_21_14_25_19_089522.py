def estritamente_crescente(listan):
    nova = []
    i = 0
    while i <= len(listan):
        if listan[i]<listan[1+i]:
            nova.append(listan[i])
            i += 1
        else:
            i += 1
    return nova
        
        