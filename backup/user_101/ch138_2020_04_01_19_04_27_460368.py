resposta1 = input("Código está executando?")
while resposta1 == "n":
    print ("Corrija o código e tente de novo")
    resposta1 = input("Código está executando?")
while resposta1 == "s":
    resposta2 = input("Código produz o resultado correto?")
    if resposta2 == "n":
        print ("Corrija o código e tente de novo e volte para o começo de tudo")
    elif resposta2 == "s":
        print ("Parabéns!")