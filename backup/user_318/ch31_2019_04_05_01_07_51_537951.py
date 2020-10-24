valor_casa=int(input("Qual é o valor da casa"))
salario=int(input("Qual eh o seu salario?"))
anos_a_pagar=int(input("O emprestimo dura quanos anos?"))
if(valor_casa/(anos_a_pagar*12)>salario*0.3):
    print("Empréstimo não aprovado")
else:
    print("Empréstimo aprovado")
    