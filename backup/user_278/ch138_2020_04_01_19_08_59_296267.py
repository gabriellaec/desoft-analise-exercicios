nao_executa=True
while nao_executa:
    pergunta1= input("Código está executando?")
    if pergunta1=="n":
        print ("Corrija o código e tente de novo")
    elif pergunta1=="s":
        pergunta2=input("Produz o resultado correto?")
        if pergunta2=="n":
            print ("Corrija o código e tente de novo e volte para o começo de tudo")
        elif pergunta2=="s":
            print ("Parabens!")
            nao_executa=False