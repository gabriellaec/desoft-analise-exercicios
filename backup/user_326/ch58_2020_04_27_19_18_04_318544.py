def conta_a(palavra):
    i = 0
    a = 0
    while i < len(palavra) - 1:
        checa_se_tem_a = palavra[i]
        if checa_se_tem_a == 'a':
            a += 1
            i += 1
        else:
            i += 1
    print(a)
    return a