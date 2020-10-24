valor = float(input()) * 1.1

unidade = int(valor)
decimo = int(valor * 10 - unidade * 10)
centesimo = int(valor * 100 - decimo * 10 - unidade * 100)

print('O valor da conta com 10%: %d.%d%d' % (unidade, decimo, centesimo))
