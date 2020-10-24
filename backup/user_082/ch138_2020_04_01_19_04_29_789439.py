#Pergunta para o usuario se o "Código está executando?"
pergunta_n_resolvida=True
while pergunta_n_resolvida:
    pergunta_1=input("Código está executando? ")

#Se a resposta for "n", diga "Corrija o código e tente de novo", volta para perguntar se o codigo esta executando
    
    if pergunta_1 == 'n':
        print("Corrija o código e tente de novo")
#Se "s", pergunte se "o código Produz o resultado correto?"
    
    elif pergunta_1 == 's': 
        pergunta_2=input("o código Produz o resultado correto?" )
#Se "n", imprima "Corrija o código e tente de novo e volte para o começo de tudo"
        if pergunta_2 == 'n':
            print("Corrija o código e tente de novo e volte para o começo de tudo")
#Se "s", imprima "Parabéns!"
        elif pergunta_2 == 's':
            print("Parabéns!")
            pergunta_n_resolvida=False