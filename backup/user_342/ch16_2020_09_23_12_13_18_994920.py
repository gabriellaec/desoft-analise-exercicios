resposta= float(input('qual o valor da conta?'))
valor=(resposta + (resposta*0.10))
texto='Valor da conta com 10%: R${0:.2f}'.format(valor)
print(texto)