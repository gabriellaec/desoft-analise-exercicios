emp=int(input('Valor do empréstimo:  '))
m=int(input('meses:  '))
tax=0.02
def calcula_valor_devido():
    return(emp*(1+tax)**m)  
print(calcula_valor_devido())