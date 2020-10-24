pergunta = input ('O código está funcionando?')
if pergunta == 'n':
    print ('Corrija o código e tente de novo')
    print (pergunta)
elif pergunta == 's':
    pergunta2 = input ('Produz o resultado correto?')
    if pergunta2 == 'n':
        print ('Corrija o código e tente de novo e volte para o começo de tudo')
        print (pergunta)
    elif pergunta2 == 's':
        print ('Parabéns!')