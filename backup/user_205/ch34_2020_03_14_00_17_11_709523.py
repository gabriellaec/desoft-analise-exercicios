def maior_primo_menor_que(n):
    contador = 1
    divisores = 0
    while (contador<n):
        contador +=1
        if (n==2):
            return 2
        if (n%contador==0):
            divisores+=1
            if (divisores==2):
                return (divisores)
        else:
            return -1