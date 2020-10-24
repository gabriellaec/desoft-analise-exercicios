pergunta=float(input("Qual foi o valor da conta do restaurante?"))
def valor(conta):
    x = pergunta+pergunta*10/100
    return x
valor_da_conta = valor(pergunta)
print ('Valor da conta com 10%: R$ {0:.2f}' .format(valor_da_conta))

    
    