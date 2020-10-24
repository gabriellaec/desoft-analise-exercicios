pergunta_funcionamento=input('O programa está funcionando? Digite sim (s) ou não(n):  ')
if pergunta_funcionamento == 's':
    print('Sem problemas!')
else:
    pergunta_correcao = input('Você sabe corrigir? Digite sim (s) ou não(n):  ')
    if pergunta_correcao == 's':
        print('Sem problemas!')
    else:
        pergunta_necessidade = input('Você precisa corrigir? Digite sim (s) ou não(n):  ')
        if  pergunta_necessidade  == 'n':
            print('Sem problemas!')
        else:
            print('Apague tudo e tente novamente')