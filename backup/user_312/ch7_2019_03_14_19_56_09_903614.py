import math
def calcula_norma(vetor):
    tamanho=0
    dimensao=len(vetor)-1
    while dimensao>0:
        tamanho=(tamanho**2+vetor[dimensao]**2)**(1/2)
        dimensao=dimensao-1
    if dimensao==1:
        return math.fabs(vetor[0])
    else:
    	return tamanho