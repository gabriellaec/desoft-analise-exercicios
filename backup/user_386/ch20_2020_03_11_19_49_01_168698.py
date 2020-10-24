a = float(input("quantos km que vc vai rodar?"))
if a >= 200:
    valor = a * 0.5
    print ('preco =','{:02.2f}'.format(valor))
else:
    valor = 100 + a*0.45
    print ('preco =','{:02.2f}'.format(valor))
    