a=int(input('Preco da casa: '))
b=float(input('Salario: '))
c=int(input('Número de anos a pagar: '))
def prestacao_mensal(a,c):
    y=a/(c*12)
    if y>0.3*b:
        return 'Empréstimo não aprovado'
    else:
        return 'Empréstimo aprovado'
print(prestacao_mensal(a,c))