pergunta=input('Código está executando?')

if pergunta=='n':
    print("Corrija o código e tente de novo" )
    pergunta=input('Código está executando?')
    
if pergunta=='s':
    pergunta2=input('Produz o resultado correto?')
    if pergunta2=='n':
        print("Corrija o código e tente de novo e volte para o começo de tudo")
    if pergunta2=='s':
        print("Parabéns!")
    
    

    
    