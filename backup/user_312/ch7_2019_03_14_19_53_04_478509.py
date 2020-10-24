import math
def calcula_norma(vetor):
    tamanho=0
    dimensao=len(vetor)
    while dimensao>1:
        tamanho=(tamanho**2+vetor[dimensao]**2)**(1/2)
        dimensao=dimensao-1
    return tamanho