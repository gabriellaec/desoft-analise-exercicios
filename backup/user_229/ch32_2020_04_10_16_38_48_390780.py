def lista_primos(n):
    if n <= 1:
        primos = [2]
    else:
        primos = [2,3]
        x = primos[1]
        for i in range(2,n):
            y = 3
            while y < (x+2):
                if (x+2)%y != 0:
                    y += 2
                else:
                    x += 2
                    break
            primos.append(x+2)
            x = primos[i]                
    return primos