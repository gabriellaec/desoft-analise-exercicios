programa = input ('O programa está funcionando? (s/n)')
if programa == 'n':
    corrigir = input ('Você sabe corrigir? (s/n)')
    if corrigir == 'n':
        precisa = input ('Você precisa corrigir? (s/n)')
        if precisa == 'n':
            print ('Sem problemas!')
        else: 
            print ('Apague tudo e tente novamente')
    else:
        print ('Sem problemas!')
else:
    print ('Sem problemas!')