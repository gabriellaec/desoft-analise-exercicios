a = True
while a == True:
    pergunta = input("Código está executando?")
    while pergunta!= 's':
        print("Corrija o código e tente de novo")
        pergunta = input("Código está executando?")
    if pergunta == 's':
        perg2 = input("Produz o resultado coreto? (s/n)")
        if perg2 == 's':
            a = False
        elif perg2 == 'n':
            pergunta = 'n'
print('Parabéns!') 
    