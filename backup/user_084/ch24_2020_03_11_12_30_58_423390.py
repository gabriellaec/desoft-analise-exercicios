S = int(input('qual o valor do salario atual: ')
def calcula_aumento(S):
    if S>1250:
        A=S*1.1
        return(A)
    else:
        A=S*1.15
        return(A)