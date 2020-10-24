def imprime_faixa(n):
    if n < 0:
        return ("nada?")
    if n < 18:
        return ("Jovem")
    elif 18 <= n < 60:
        return ("Adulto")
    elif n >= 60:
        return ("Idoso")
    
    