def calcula_valor_devido(v_e, n_m,t_j):
    if (n_m !=0) or (v_e != 0) and (t_j != 0):
    	v_d = v_e * ((1 + t_j)**n_m)
    elif (v_e != 0):
        v_d = v_e * ((1 + t_j)**n_m)
    else:
        v_d = v_e * ((1 + t_j)**n_m)
    return v_d
	
