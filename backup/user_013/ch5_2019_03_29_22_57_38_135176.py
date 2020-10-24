from math import sqrt
def maior_primo_menor_que(n):
    #Criando variável de teste, k:
    k = n
    #Criando uma Variável de teste booleana, t:
    T = True
    #Criando um looping para testar se k é primo ou não:
    while T:
        #Criando a varredura de testes 
        A = [0] 
        for i in range(1,k):
            if k % i == 0:
                A.append(i)
        if len(A) > 2:
            k -= 1
        else:
            T = False
    if k > 1:
        return k
    else:
        return -1