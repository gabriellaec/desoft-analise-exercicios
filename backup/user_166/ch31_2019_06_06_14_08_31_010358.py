valor_casa_comprar=int(input("qual o valor da casa a comprar?"))
salário= int(input("qual o salário?"))
quantidade_anos_a_pagar= int(input("pagar em quantos anos?"))
quantidade_meses_a_pagar= quantidade_anos_a_pagar * 12
prestação_mensal= valor_casa_comprar/ quantidade_meses_a_pagar
if prestação_mensal > salário*1.3:
    print("Empréstimo não aprovado")
else:
    print("Empréstimo aprovado")
    