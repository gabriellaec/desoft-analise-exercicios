j=True
while j==True:
    x=input("Código está executando? s/n?")
    if x=='n':
        print("Corrija o código e tente de novo")
        j==True
    elif x=='s':
        y=input("O código produz o resultado certo? s/n?")
        if y=='n':
            print("Corrija o código e tente de novo")
            j==True
        elif y=='s':
            print ("Parabéns!")
            j==False