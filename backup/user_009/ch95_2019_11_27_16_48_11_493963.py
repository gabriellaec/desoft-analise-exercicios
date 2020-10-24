def mais_populoso(brasil):
    dic_r = {}
    for estado in brasil:
        soma = 0 
        dic_est = brasil[estado]
        for num_hab in dic_est:
            soma += dic_est[num_hab]
        dic_r[estado] = soma
    return dic_r
            
