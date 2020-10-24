input("Qual é a velocidade do seu carro em km?")
def velocidade_do_carro(velocidade):
    if velocidade > 80:
        return (velocidade - 80)*5
    	return "Você foi multado"
    else:
        return "Você não foi multado"
print(velocidade_do_carro(velocidade))