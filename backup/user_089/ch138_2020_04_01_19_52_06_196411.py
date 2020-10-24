
executando = True

while executando:
    codigo = input("Código está executando?")
    if codigo == "n":
        print("Corrija o código e tente de novo")
    
    else :
        executando = False
        resultado = input("O resultado está correto?")
        if resultado == "n":
            print("Corrija o código e tente de novo e volte para o começo de tudo")
        else:
            print("Parabéns!")
            