v_acomprar = input('Qual o valor da casa aser comprada? ')
salario = input('Qual o seu salário? ')
anos = input('Em quantos anos será pago? ')
def prestac(v_acomprar, anos):
    mensal = v_acomprar/(anos*12)
    limite = 0.30*salario
    for mensal <= limite:
        return mensal
    