executando = str(input("Código está executando? ")
    if executando == 's':
        resultado = str(input("Produz o resultado correto? "))
            if resultado == 's':
                 print("Parabéns!")
            elif resultado == 'n':
                 print("Corrija o código e tente de novo e volte para o começo de tudo")
                 continue
    if executando == 'n':
        print("Corrija o código e tente de novo e volte para o começo de tudo")
        continue