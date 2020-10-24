a = float(input("Qual é a velocidade do seu carro em km?   "))
def velocidade_do_carro(velocidade):
    if velocidade > 80:
        multa = (velocidade - 80)*5
        return "Você foi multado. Sua multa é {:0.2f}".format(multa)
    else:
        return "Você não foi multado"
print(velocidade_do_carro(a))