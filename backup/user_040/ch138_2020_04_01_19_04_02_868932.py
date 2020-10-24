programa = True
while programa == True:
    execucao_codigo = input("Código está executando?(n/s) ")
    if execucao_codigo == "s":
        resultado_correto = input("Produz o resultado correto?(n/s) ")
        if resultado_correto == "s":
            print ("Parabéns")
            programa = False
        else:
            print ("Corrija o código e tente de novo e volte para o começo de tudo")
    else:
        print ("Corrija o código e tente de novo")