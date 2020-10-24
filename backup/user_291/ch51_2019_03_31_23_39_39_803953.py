def estritamente_crescente(lista):
    i = 0
    outro = []
    maior = 0
    while i < len(lista):
        if lista[i] > maior:
            outro.append(lista[i])
            maior = lista[i]
        i += 1
    return outro
        
        
  