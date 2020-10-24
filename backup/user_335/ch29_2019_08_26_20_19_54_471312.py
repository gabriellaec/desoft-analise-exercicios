def calcula_aumento(salario):
    if (salario > 1250):
        valor = salario * 1.1
        return valor
    else:
        valor = salario*1.15
        return valor

valorUser = float(input("Digite o valor do seu salário: "))
print ("Seu novo salário é: {0:.2f}" .format(calcula_aumento(valorUser)))