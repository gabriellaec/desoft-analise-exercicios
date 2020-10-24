v_acomprar = float(input('Qual o valor da casa a ser comprada? '))
salario = float(input('Qual o seu salário? '))
anos = float(input('Em quantos anos será pago? '))
def prestac(v_acomprar, anos):
    mensal = v_acomprar/(anos*12)
    limite = 0.30*salario
    if mensal <= limite:
        return mensal
    