

def maior_primo_menor_que(n):
    if n<0:
        return -1
    else:
        for i in range(0,n+1):
            if eh_primo(i):
                lista_primos.append(i)
                maiorprimo=lista_primos[-1]
        return maiorprimo
