pergunta1=input('Está funcionando?')
if pergunta1 == 's':
    print('Sem problemas!')
elif pergunta1 == 'n':
    pergunta2=input('Você sabe corrigir?')
    if pergunta2 == 's':
        print('Sem problemas!')
    elif pergunta2 == 'n':
        pergunta3=input('Você precisa corrigir?')
        if pergunta3 == 'n':
            print('Sem problemas!')
        elif pergunta3 == 's':
            print('Apague tudo e tente novamente')
    
       
    
