flux = True
while flux == True:

    per = input ('O código está executando?')
    while per != 's':
        print ('Corrija o código e tente de novo.')
        per = input ('O código está executando?')
    if per == 's':
        per2 = input ('Produz o resultado correto?')
        if per2 == 's':
            flux = False
        elif per2 == 'n':
            print ('Corrija o código e tente de novo.')
            pergunta = 'n'
print ('Parabéns!')
            
          
            
        
