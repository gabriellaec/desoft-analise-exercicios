def lista_primos(n):
    primos =[]
    j=0
    while j >= n:
        i= 3
        if (j % 2) == 0 and j != 2 or j == 1 or j == 0:
            break
        while j > i:
            if (j % i) == 0:
                break
            i += 2
        primos.append(j)
        j +=1
        
    return primos   
