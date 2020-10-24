codigo = input("Código está executando?")

while codigo == "n":
    print ("Corrija o código e tente de novo")
    codigo = input("Código está executando?")
    if codigo == "s":
        pergunta = input("O código produz o resultado correto?")
        while pergunta == "n":
            print ("Corrija o código e tente de novo e volte para o começo de tudo")
            pergunta = input("O código produz o resultado correto?")
            if pergunta == "s":
                print ("Parabéns!")

if codigo == "s":
    pergunta = input("O código produz o resultado correto?")
    while pergunta == "n":
        print ("Corrija o código e tente de novo e volte para o começo de tudo")
        pergunta = input("O código produz o resultado correto?")
        if pergunta == "s":
            print ("Parabéns!")