codigo = input("Código está executando?")

while codigo == "n":
    print ("Corrija o código e tente de novo")
    codigo = input("Código está executando?")
    while codigo == "s":
        pergunta = input("O código produz o resultado correto?")
        if pergunta == "n":
            print ("Corrija o código e tente de novo e volte para o começo de tudo")
        if pergunta == "s":
            print ("Parabéns!")
break