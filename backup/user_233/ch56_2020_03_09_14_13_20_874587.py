from math import sqrt

def calcula_norma(vetor):
    
    if len(vetor) <= 2:
       	vetor.append(0)
	if len(vetor) <= 1:
       	vetor.append(0)
    if len(vetor) == 0:
        vetor.append(0)
    
    vetor[0] *= vetor[0]
    vetor[1] *= vetor[1]
    vetor[2] *= vetor[2]
    
    return sqrt(sum(vetor))
    
    
    
    