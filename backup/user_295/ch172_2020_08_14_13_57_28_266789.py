def int(imprime_faixa(n)):
    if n < 18:
        return ("Jovem")
    elif 18 <= n < 60:
        return ("adulto")
    elif n > 60:
        return ("idoso")
    