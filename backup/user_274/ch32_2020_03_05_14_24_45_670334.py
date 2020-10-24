def lista_primos(num):
    i=3
    if num == 1 or num == 0:
        return "Nenhum primo"
    
    primo = [2]

    while i <= num:
        j=2
        c=0
        while j < i:
            if i%j != 0:
                c=c+1
            j=j+1
        if c+2 == j:
            primo.append(j)
        i=i+1
    return primo