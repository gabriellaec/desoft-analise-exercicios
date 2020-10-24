x=input('código está executando ? ')
y=input('O código está produzindo o resultado certo ? ')
while y!='s':    
    if x =='n':
        print('corrija o código e tente novamnete')
        x =input('código está executando ? ')
    if x =='s':
        y=input('O código está produzindo o resultado certo ? ')
        if y=='n':
            print('Corrija o código e tente de novo e volte para o começo de tudo')
        if y=='s':
            print("Parabéns!")
