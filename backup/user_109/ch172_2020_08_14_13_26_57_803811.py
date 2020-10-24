def imprime_faixa(n):
    if n < 0:
        return "inválido"
    elif n >= 0 and n < 18:
        return "jovem"
    elif n >= 18 and n < 60:
        return "adulto"
    elif n >= 60:
        return "idoso"