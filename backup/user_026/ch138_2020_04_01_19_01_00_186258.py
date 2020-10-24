
while True:
    pergunta=("Código está executando?")
    if pergunta=="n":
        print("Corrija o código e tente de novo")
        pergunta=("Código está executando?")
        if pergunta =="s":
            pergunta_resultado=input(" o código Produz o resultado correto?")
            if pergunta_resultado=="n":
                print("Corrija o código e tente de novo e volte para o começo de tudo")
            if pergunta_resultado=="s":
                print("Parabéns!")
