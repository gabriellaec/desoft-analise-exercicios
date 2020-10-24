def calcula_valor_devido (valor, meses, taxa):
    if meses == 0:
        return 'O número de meses não pode ser zero.'
    elif valor == 0:
        return 'O valor não pode ser zero.'
    elif taxa == 0:
        return 'A taxa não pode ser igual a zero.'
    else:
        valor_devido = (valor * ((1 + taxa) ** meses))
        return valor_devido

