x = input('Tem dúvida:')
if x=='não':
    print('Pratique mais') and tem_duvida = False
else:
    tem_duvida = True
while tem_duvida:
    x = input('Tem dúvida:')
    if x=='não':
        print('Pratique mais') and tem_duvida = False
    else:
        tem_duvida = True
print('Até a próxima')