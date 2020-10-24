def teytey(valor):
    novo_valor=valor*0.10+valor
    return novo_valor
valor=float(input('Qual o valor da conta?: '))
print(('Valor da conta com 10%: R$ {:.2f}' .format(teytey(valor))))