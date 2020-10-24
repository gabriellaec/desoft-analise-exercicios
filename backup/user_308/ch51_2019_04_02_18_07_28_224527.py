def estritamente_crescente(numeroes):
    maior=0
    crescente=[]
    for e in numeroes:
        if e>maior:
            crescente.append(e)
            maior=e
    return crescente