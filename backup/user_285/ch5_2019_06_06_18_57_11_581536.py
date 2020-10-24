def eh_primo(num):
    n=3
    while n<num:
        if num%2==0 or num%n==0:
            return False
        n+=2
    if num==0 or num==1:
        return False
    
    else:
        return True

lista_primos=[]

def maior_primo_menor_que(n):
    if n<0:
        return -1
    else:
        for i in range(0,n+1):
            if eh_primo(i):
                lista_primos.append(i)
                maiorprimo=lista_primos[-1]
        return maiorprimo
