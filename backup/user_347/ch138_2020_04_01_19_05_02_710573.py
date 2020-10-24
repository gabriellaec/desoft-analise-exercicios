one = True
while one:
    one = input ("Código está executando? (s/n)")
    if one == "n":
        print("Corrija o código e tente de novo")
        one = True
    if one == "s":
        two= input("Produz o resultado correto? (n/s)")
        one = False
        if two == "n":
            print("Corrija o código e tente de novo e volte para o começo de tudo")
            one = True
        if two == "s":
            print("Parabéns")
            
            