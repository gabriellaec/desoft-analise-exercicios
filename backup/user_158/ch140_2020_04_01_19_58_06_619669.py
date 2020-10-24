def faixa_notas(lista):
    not_inf = 0
    not_ate = 0
    not_sup = 0
    for nota in lista:
        if nota > 7:
            not_sup += 1
        elif nota < 5 :
            not_inf += 1 
        else:
            not_ate += 1 

    Lista_output = [not_inf, not_ate, not_sup]
    return Lista_output