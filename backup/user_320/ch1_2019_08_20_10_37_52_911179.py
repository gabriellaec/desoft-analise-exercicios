def valor_devido(principal, juros, meses):
    vf = ((principal * (juros / 100))**(meses / 12))
    return vf