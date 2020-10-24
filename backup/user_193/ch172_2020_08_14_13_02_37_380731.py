def imprime_faixa(n):
    if n<18:
        return "jovem"
    elif n<60:
        return "adulto"
    elif n>=60:
        return "idoso"
    else:
        return "Digite um valor válido."