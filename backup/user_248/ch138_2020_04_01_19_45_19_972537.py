def jogo(x):
    x=input("Código está executando? s/n?")
    if x=='n':
        print("Corrija o código e tente de novo")
        jogo=True 
    if x=='s':
        y=input("O código produz o resultado certo? s/n?")
        if y=='n':
            print("Corrija o código e tente de novo")
            jogo=True
        elif y=='s':
            print ("Parabéns!")
            jogo=False