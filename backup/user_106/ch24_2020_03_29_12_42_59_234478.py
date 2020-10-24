s=int(input('Digite o salário: '))

def calcula_aumento(s):
    if s>1250:
        x=s*1.1
        return x
    elif s<=1250:
        x=s*1.15
        return x
        