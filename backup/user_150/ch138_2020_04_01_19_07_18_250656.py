codigofunciona = False

while codigofunciona == False:
    perguntaaluno = input("Código está executando? ")
    if perguntaaluno == 'n':
        print("Corrija o código e tente de novo")
    elif perguntaaluno == 's':
        perguntadois = input("Produz o resultado correto? ")
        if perguntadois == "n":
            print("Corrija o código e tente de novo e volte para o começo de tudo")
        elif perguntadois == "s":
            print("Parabéns!")
            codigofunciona = True