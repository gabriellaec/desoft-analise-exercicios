emp=float(input("digite o valor do empréstimo"))
divida=int(input("digite em quantos anos pagará"))*12
salario=float(input("digite o salário"))

def funcao(emp,divida,salario):
    por_do_sal=((30/100)*salario)
    prestacao=(emp/divida)
    if prestacao>por_do_sal:
        return "Empréstimo não aprovado"
    else:
        return "Empréstimo aprovado"
    
print(funcao(emp,divida,salario))