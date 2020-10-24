def maior_primo_menor_que(n):
    i=2
    primos = []
    while n >= i:
        resto = n%i
        if resto == 0:
            pass
        else:
            primos.append(i)
        i += 1
   	return(primos[-1])