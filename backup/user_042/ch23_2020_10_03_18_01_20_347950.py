pergunta_velocidade = (input('Qual a velocidade do seu carro?')
if pergunta_velocidade > 80:
    valor_a_pagar = (pergunta_velocidade - 80) * 5
    return ('Multado em {0:.2f}'.format(valor_a_pagar))
else: 
    return (Não foi multado)