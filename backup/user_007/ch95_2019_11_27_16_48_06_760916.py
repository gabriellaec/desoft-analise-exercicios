def mais_populoso(dic):
    #emp = Estado mais populoso
    emp = 'Sao Paulo'
    max = 0
    soma = 0
    for i in dic:
        for j in dic[i].values():
            soma += j
        if soma >= max:
            max = soma
            emp = i
        soma = 0
    return emp