def faixa_notas(l1):
    lista = []
    a , b , c = 0
    for i in l1:
        if i < 5:
            a +=1
        if 5 <= i and i <= 7:
            b += 1
        if i >= 7:
            c += 1
    lista = a,b,c 
    return lista 
     