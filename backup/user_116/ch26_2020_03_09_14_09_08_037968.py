def aprovacao(casa,salario,anos):
    if prestacao>(30/100)*salario:
        return ('Empréstimo não aprovado')
    else:
        return ('Empréstimo aprovado')


casa=int(input("valor da casa ?"))
salario=int(input("qual seu salario?"))
anos=int(input("quantos anos?"))
prestacao=(casa)/(anos)
print(aprovacao(casa,salario,anos))