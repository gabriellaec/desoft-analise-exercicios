resposta = False
while resposta != True:
    resposta = str(input("Código está executando?"))
    if resposta == "n":
                   print("Corrija o código e tente de novo")
    elif resposta == "s":
                   resposta2 = str(input("O código produz o resultado correto?"))
                   if resposta2 == "n":
                                   print("Corrija o código e tente de novo e volte para o começo de tudo")
                   elif resposta2 == "s":
                                   print("Parabéns")
                                   resposta = True
               