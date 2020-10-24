S=int(input("digite o Salario"))
def calcula_aumento(S):
    if S>1250:
        return (S*1.1)-S
    else:
        return (S*1.15)-S