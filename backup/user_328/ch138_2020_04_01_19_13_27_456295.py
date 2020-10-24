condicao=True 
while condicao:
    a= input('Código está executando(s/n)? ')
    if a == 'n':
        print('Corrija o código e tente de novo')
        condicao= True 
    elif a == 's':
        b= input('Produz o resultado correto(s/n)? ')
        if b == 's':
            print('Parabéns!')
            condicao= False
        elif b == 'n':
            print('Corrija o código e tente de novo')
            condicao= True 
    

        
    