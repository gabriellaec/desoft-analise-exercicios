print('---------------------------------------------------------------')
print('Valor da conta:')
valor = float(input())

valor_final = (valor + valor*0.1)

print('---------------------------------------------------------------')
print('Valor da conta com 10%: R${:.2f}' .format(valor_final))