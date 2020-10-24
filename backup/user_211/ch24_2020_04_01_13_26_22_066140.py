def calcula_aumento():
    s=float(input("qual o seu salário?"))
    if s>1250:
        ns=1.1*s
    else:
        ns=1.15*s
    return ns