def fatorial(n):
    contador=1
    resultado=1
    while contador<=p:
        resultado*=contador
        contador+=1
    return resultado
p=int(input("numero"))    
print(fatorial(p))