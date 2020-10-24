import math
def calcula_pi(n):
    i=1
    soma=0
    while i<=n:
        soma = soma + 6/(i**2)
        i+=1
    pi = math.sqrt(soma)
    return pi
#3: resolução correta!!!
lista = [2,3,4,5,10]
def classifica_lista(lista):
    if len(lista)<2:
        return 'nenhum'
    i=0
    while i in range(i,len(lista)):
        while lista[i] <= lista[i+1]:
            i+=1
            if i == len(lista) -1:
                return 'crescente'
            if lista[i] > lista[i+1]:
                return 'nenhum'
        while lista[i] >= lista[i+1]:
            i+=1
            if i == len(lista) -1:
                return 'decrescente'
            if lista[i] < lista[i+1]:
                return 'nenhum'
        else:
            return 'nenhum'
