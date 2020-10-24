pergunta1 = str(input('Está Funcionando?'))
if pergunta1 == 's':
    print('Sem problemas!')
elif pergunta1 == 'n':
    pergunta2 = str(input('Você sabe corrigir? (n/s)'))
    if pergunta2 == 's':
        print('Sem problemas!')
    elif pergunta == 'n':
        pergunta3 = str(input('Você precisa corrigir? (n/s)'))
        if pergunta3 == 's':
            print('Apague tudo e tente novamente')
        elif pergunta3 == 'n':
            print('Sem problemas!')