km=int(input('quantos km vao ser?'))
if km <= 200:
    preço= km*0.5
else:
    preço= ((km-200)*45)+(0.5*200)
print('O valor da passagem formatada é {:.2f}'.format(preço))