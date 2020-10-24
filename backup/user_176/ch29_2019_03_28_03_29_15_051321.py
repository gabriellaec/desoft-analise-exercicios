def calcula_aumento(v):
    sal = v
    if v > 1250:
        a=1250+0.1*1250
    else:
        a=v+0.15*v
    return sal
