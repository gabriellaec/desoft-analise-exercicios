terminou = False
while terminou != True:
    resposta = input("Código está executando?")
    if resposta == 'n' or resposta == ' n':
        print("Corrija o código e tente de novo")
    if resposta == 's' or resposta == ' s':
        resposta = input("Produz o resultado correto?")
        if resposta == 'n' or resposta == ' n':
            print("Corrija o código e tente de novo e volte para o começo de tudo")
        if resposta == 's' or resposta == ' s':
            print("Parabéns!")
            terminou = True