a =True
while a:
    pergunta1 = input ("Código está executando? (Digite n ou s).")
    if pergunta1 == "n":
        print("Corrija o código e tente de novo")
        a = True

    elif pergunta1 == "s":
        pergunta2 = input("O código produz o resultado correto? (Digite s ou n).")
        if pergunta2 == "s":
            print("Parabéns!")
            a = False
        elif pergunta2 == "n":
            print ("Corrija o código e tente de novo e volte para o começo de tudo.")
            a = True