emp=int(input("digite o valor do empréstimo"))
divida=int(input("digite em quantos anos pagará"))
salario=int(input("digite o salário"))

def funcao(emp,divida,salario):
    por_do_sal=((30/100)*salario)
    prestacao=(emp/divida)
    if prestacao>por_do_sal:
        return "Empréstimo não aprovado"
    elif prestacao<=por_do_sal:
        return "Empréstimo aprovado"
    
print(funcao(emp,divida,salario))