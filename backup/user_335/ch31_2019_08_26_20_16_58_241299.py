def emprestimo(casa, salario, anos):
    prestacao = casa/(anos*12)
    if (prestacao <= (salario*0.3)):
        return print ('Empréstimo aprovado')
    else:
        return print ('Empréstimo não aprovado')
    
Vcasa = int(input("Digite o valor da casa: "))
Vsalario = int(input("Digite o seu salário: "))
Vanos = int(input("Quantos anos você deseja pagar: "))

emprestimo(Vcasa,Vsalario,Vanos)
 