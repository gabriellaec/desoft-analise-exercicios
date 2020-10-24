tem_duvidas = True
while tem_duvidas:
    resposta = input("Código está executando?")
    if resposta == 'n':
        print("Corrija o código e tente de novo")
    elif resposta == 's':
        pergunta = input("Código produz resultado correto?")
        if pergunta == 'n':
            print("Corrija o código e tente de novo e volte para o começo de tudo")
        else:
            print("Parabéns!")
            break