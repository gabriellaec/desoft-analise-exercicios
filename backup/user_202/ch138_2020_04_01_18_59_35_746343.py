while True:
    p1 = input("Código está executando?")
    if p1 == 'n':
        print("Corrija o código e tente de novo")
    else:
        p2 = input("Produz o resultado correto?")
        if p2 == 'n':
            print("Corrija o código e tente de novo e volte para o começo de tudo")
        else:
            print("Parabéns!")
            break