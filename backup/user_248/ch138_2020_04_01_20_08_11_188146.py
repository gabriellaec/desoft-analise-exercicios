def jogo(x):
    x=input("Código está executando? s/n?")
    j=True
    while x=='n':
        print("Corrija o código e tente de novo")
        j==True
    while x=='s':
        y=input("O código produz o resultado certo? s/n?")
        if y=='n':
            print("Corrija o código e tente de novo")
            j==True
        elif y=='s':
            print ("Parabéns!")
            j==False