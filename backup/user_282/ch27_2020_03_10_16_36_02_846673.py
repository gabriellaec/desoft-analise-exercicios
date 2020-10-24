tem_duvidas = True

while tem_duvidas:
   
    resposta = input('voce esta com duvidas? ')
   
    if resposta != 'não':
        print('Pratique mais')
	
    else:
        tem_duvidas = False
else:
    print('Até a próxima')