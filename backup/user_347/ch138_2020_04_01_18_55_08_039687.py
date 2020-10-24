one=input ("Código está executando? (s/n)")
if one == "n":
    print("Corrija o código e tente de novo")
    one=input ("Código está executando? (s/n)")
if one == "s":
    two= input("Produz o resultado correto? (n/s)")
    if two == "n":
        print("Corrija o código e tente de novo e volte para o começo de tudo")
    if two == "s":
        print("Parabéns")