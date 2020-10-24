def calcula_aumento(s,a):
    a = 0 
    if s > 1250:
        a = s*0.10
    else:
        a = s*0.15 
    return a
    