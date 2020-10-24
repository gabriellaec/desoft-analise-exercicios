def faixa_notas(notas):
    a = 0
    b = 0
    c = 0
    for i in notas:
        if i < 5:
            a += 1
        elif i <= 7:
            b += 1
        else:
            c += 1
    return [a ,b ,c]