def imprime_faixa(n):
    if n < 0:
        print("inválido")
    elif n >= 0 and n < 18:
        print("jovem")
    elif n >= 18 and n < 60:
        print("adulto")
    elif n >= 60:
        print("idoso")