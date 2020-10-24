while True:
    verif_cod = input("Código está executando?")
    if verif_cod == 'n':
        print("Corrija o código e tente de novo")
    elif verif_cod == 's':
        resultado_correto = input("Produz o resultado correto?")
        if resultado_correto == 's':
            print("Parabéns!")
            break
        elif resultado_correto == 'n':
            print("Corrija o código e tente de novo e volte para o começo de tudo")
