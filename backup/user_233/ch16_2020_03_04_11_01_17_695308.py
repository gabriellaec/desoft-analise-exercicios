valor = float(input())

unidade = int(valor)
decimo = int(valor * 10 - unidade * 10)
centesimo = int(valor * 100 - decimo * 10 - unidade * 100)

print('Valor da conta com 10%: R$ %d.%d%d' % (unidade, decimo, centesimo))
