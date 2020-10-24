resposta=input('Tá com dúvida:')
if resposta!='não':
    tem_duvida= True
while tem_duvida:
    print('Pratique mais')
    resposta=input('Tá com dúvida:')
    if resposta=='não':
        tem_duvida = False
    else:
        tem_duvida = True
print('Até a próxima')