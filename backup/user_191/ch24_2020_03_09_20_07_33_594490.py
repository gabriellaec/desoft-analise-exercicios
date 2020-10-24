def calcula_aumento(s):
    s=float(input('salario'))
    if s>1250:
        n=s*1.1
        return n
    else:
        n=s*1.15
        return n