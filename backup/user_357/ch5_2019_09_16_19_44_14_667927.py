def primo_ou_nao(numero):
    i=1 
    while numero % i == 0:
        i+=1
    if i - 1 > 1 and  i < numero:
        return False 
    else:
        return True
    
def maior_primo_menor_que(n):
    if n <= 0:
        return -1  
    else: 
        primo_mais_proximo = n 
        while primo_ou_nao(primo_mais_proximo) == False:
            primo_mais_proximo-=1