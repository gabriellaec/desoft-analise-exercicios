def encontra_maximo(lista):
    maior=-1000
    for e in lista[:]:
        if e>maior:
            maior=e
    return maior
        
    