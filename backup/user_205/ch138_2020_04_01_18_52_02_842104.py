a = 0
while a!=1:
    pergunta = input("Código está executando? ")
    if pergunta == "n":
        print ("Corrija o código e tente de novo")
        a = 0
    elif pergunta == "s":
        pergunta2 = input("O código produz o resultado correto? ")
        if pergunta2=="n":
            print ("Corrija o código e tente de novo e volte para o começo de tudo")
            a = 0
        else:
            print ("Parabéns!")
            a = 1
            