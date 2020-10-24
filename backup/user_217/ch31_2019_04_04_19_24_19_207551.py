def valor_da_prestação(a,b,c):
      
    x=a/c

    if x >= (0.3 * b):
        resultado = 'Empréstimo não aprovado'
    else:
        resultado = 'Empréstimo aprovado'
        return resultado
a=int(input('Qual o valor da casa?: '))
b=int(input('Qual é o seu salario?: '))
c=int(input('Qual a quantidade de anos a pagar?: '))
print(valor_da_prestação(c,b,a))
    