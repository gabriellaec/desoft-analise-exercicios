executando=input("Código está executando ?")
while True:
    if executando!="s":
        correto=input("Produz o resultado correto?(n/s)")
        if correto=="s":
            print("Parabéns")
            break
        else:
            print("Corrija o código e tente de novo")
    else:
        print("Corrija o código e tente de novo")