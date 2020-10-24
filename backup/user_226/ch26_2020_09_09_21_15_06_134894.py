valor = int(input("Qual o valor da casa? "))
salario = int(input("Qual o salario? "))
anos = int(input("Quantos anos? "))

def calcula_prestacao(valor, anos):
    meses = anos * 12
    prestacao = valor / meses
    return prestacao

def aprova(prestacao, salario):
    if prestacao > (salario * 0.3):
        print('Empréstimo não aprovado')
    else:
        print('Empréstimo aprovado')
        
prestacao = calcula_prestacao(valor, anos)
aprova(prestacao, salario)
