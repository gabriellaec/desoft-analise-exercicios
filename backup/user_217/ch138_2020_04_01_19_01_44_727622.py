comeco=True
while comeco:
    pergunta = input("Código está executando?")
    if pergunta == 's':
        sim=True
        while sim:
            pergunta_2=input("O código produz o resultado correto?")
            if pergunta_2 == 's':
                print("Parabéns!")
                sim=False
                comeco = False
            else:
                print("Corrija o código e tente de novo e volte para o começo de tudo")
                sim=False
    else:
        print("Corrija o código e tente de novo")
        comeco = True