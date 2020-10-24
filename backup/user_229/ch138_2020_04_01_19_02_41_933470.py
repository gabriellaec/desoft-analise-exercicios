continuar = True
executando = str(input("Código está executando? "))
while continuar == True:
    if executando == 's':
        resultado = str(input("Produz o resultado correto? "))
        if resultado == 's':
            print("Parabéns!")
            continuar = False
        elif resultado == 'n':
            print("Corrija o código e tente de novo e volte para o começo de tudo")
            continuar = True
    elif executando == 'n':
        print("Corrija o código e tente de novo e volte para o começo de tudo")
        continuar = True