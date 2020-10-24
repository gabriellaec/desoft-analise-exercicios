resposta1 = str(input('Está funcionando?(n/s)'))
respondendo = True
if resposta1 == 's':
    print('Sem problemas!')
    respondendo = False
else: 
    respondendo = True
    resposta2 = str(input('Você sabe corrigir(n/s)'))
    if resposta2 == 's':
        print ('Sem problemas!')
        respondendo = False
    else:
        respondendo = True
        resposta3 = str(input('Você precisa corrigir?(n/s)'))
        if resposta3 == 's':
            print('Apague tudo e tente novamente!')
            respondendo = False
        else:
            print('Sem problemas!')
            respondendo = False