def fatorial(x):
    mult = 1
    for item in range(1, x+1):
        mult *= item
    return mult

def calcula_euler(x,n):
    lista = [1,x]
    contador = 2
    while len(lista) < n:
        fator = x**(contador)/fatorial(contador)
        contador += 1
        lista.append(fator)
    
    return sum(lista)