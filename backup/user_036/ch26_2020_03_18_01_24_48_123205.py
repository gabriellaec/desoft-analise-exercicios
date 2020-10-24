casa= int(input('Qual o valor da casa? '))
salario= int(input('Qual o seu salario? '))
anos= int(input('Em quantos anos voce quer pagar? '))
def emprestimo(casa,salario,anos):
    x=casa/(anos*12)
    if x<=0.3*salario:
        return('Empréstimo aprovado')
    else:
        return('Empréstimo não aprovado')
print(emprestimo(casa,salario,anos))