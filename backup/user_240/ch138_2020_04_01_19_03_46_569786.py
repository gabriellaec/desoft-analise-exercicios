while 1:
    while 1:
        print("Código está executando?")
        resposta = input()
            if resposta == 's':
                break
            else:
                print("Corrija o código e tente de novo")
    print("Produz o resultado correto? (n/s)")
    resposta = input()
    if resposta == "s":
        break
    else:
        print("Corrija o código e tente de novo e volte para o começo de tudo")
print("Parabéns!")