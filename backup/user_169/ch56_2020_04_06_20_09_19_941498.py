def calcula_norma(lista):
    soma=0
    
    for i in lista:
        soma+=i**2
        
    return soma**(1/2)