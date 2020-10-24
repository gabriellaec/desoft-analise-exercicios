contador = True
while contador:
    resposta1 = input("Código está executando?")
    if resposta1 == "n":
        print("Corrija o código e tente de novo")
        continue
    elif resposta1 == "s":
        resposta2 = input("Produz o resultado correto?")
        if resposta2 == "n":
            print("Corrija o código e tente de novo e volte para o começo de tudo")
            continue
        elif resposta2 == "s":
            contador = False
print("Parabéns!")
    