executando=True
while executando:
    codigo = input("Código está executando?")
    if codigo == 's':
        loop2 = True
        while loop2:
            produz = input("O código produz o resultado correto?")
            if produz == 's':
                print("Parabéns!")
                loop2 = False
                executando = False
            else:
                print("Corrija o código e tente de novo e volte para o começo de tudo")
                loop2 = False
    else:
        print("Corrija o código e tente de novo")
        executando = False