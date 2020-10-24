def calcula_valor_devido(v_e, n_m,t_j):
    if (v_e <= 0) or (n_m <=0) or (t_j <= 0):
        return 'Valores Inválidos'
    v_d = v_e * ((1 + t_x)**2)
    return v_d