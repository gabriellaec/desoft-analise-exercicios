Encerrar = 0
while Encerrar == False:
    a = input("Código está executando? ")
    if a == 's':
        b = input("Produz o resultado correto? ")
        if b == 's':
            print("Parabéns! ")
            Encerrar = True
        if b == 'n':
            print("Corrija o código e tente de novo")
            Encerrar = False
    if a == 'n':
        print("Corrija o código e tente de novo")
        Encerrar = False