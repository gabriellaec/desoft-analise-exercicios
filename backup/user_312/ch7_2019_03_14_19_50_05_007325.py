import math
def calcula_norma(vetor):
    if len(vetor)==1:
        return (vetor)
    elif len(vetor)==2:
        return (vetor[0]**2+vetor[1]**2)**(1/2)
    elif len(vetor)==3:
        return ((vetor[0]**2+vetor[1]**2)+vetor[2]**2)**(1/2)