km=int(input('quantos km vao ser?'))
if km <= 200:
    preço= km*0.5
else:
    preço= (km-200)*0.45+200*0.5
print('O valor da passagem formatada é {:.2f}'.format(preço))