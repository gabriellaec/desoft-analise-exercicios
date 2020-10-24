x = True
while x:
    pergunta=("Código está executando? (s/n) ")
    if pergunta=="n":
        print("Corrija o código e tente de novo")
        x= True
        
    elif pergunta =="s":
        pergunta_resultado=input(" o código Produz o resultado correto? (s/n) ")
        if pergunta_resultado=="s":
            print("Parabéns!")
            x= False
        elif pergunta_resultado=="n":
            print("Corrija o código e tente de novo e volte para o começo de tudo")
            x= True


