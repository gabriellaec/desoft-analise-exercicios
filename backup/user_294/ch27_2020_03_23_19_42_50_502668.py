tem_duvidas = True
if tem_duvidas:
    resposta = input ('voce tem duvidas? ')
    if resposta == 'nao':
        tem_duvidas = False
        print ('ok')
    else:
        print ('pratique mais')
while tem_duvidas:
    resposta = input ('voce esta com duvidas? ')    
    if resposta == 'nao':
        tem_duvidas = False
        print ('ok')
    else:
        print ('pratique mais')