respostaUm = str(input('O programa está funcionando?(s/n) '))
if respostaUm == 's':
    print ('Sem problemas!')
else:
    
    respostaDois = str(input('Você sabe corrigir?(s/n) '))
    if respostaDois == 's':
        print ('Sem problemas!')
    else:
        
        respostaTres = str(input('Você precisa corrigir?(s/n) '))
        if respostaTres == 'n':
            print ('Sem problemas!')
        else:
            print ('Apague tudo e tente novamente')
        