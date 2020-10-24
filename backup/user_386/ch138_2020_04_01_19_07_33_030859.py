executando=True
while executando:
    codigo = input("Código está executando?")
    if codigo == 's':
        loop2 = True
        while pro:
            produz = input("O código produz o resultado correto?")
            if produz == 's':
                print("Parabéns!")
                loop2 = False
                executando = False
            else:
                loop2 = False
                print("Corrija o código e tente de novo e volte para o começo de tudo")
    else:
        executando = False
        print("Corrija o código e tente de novo")