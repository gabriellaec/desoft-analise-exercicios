def imprime_faixa(idade):
    if   idade <0:
        return "nao eh inteiro"
    elif idade < 18:
        return 'jovem'
    elif idade < 60:
        return 'adulto'
    else:
        return 'idoso'