def pergunta():
    x=float(input("Qual a velocidade? "))
    if float(x)>80: 
        multa=(x-80)*5
        print("Sua multa é: ",multa)