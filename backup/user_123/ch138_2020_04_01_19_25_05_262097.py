t = True
while t == True:
    pergunta1 = input("Código está executando?")
    while pergunta1 != "s":
        print ("Corrija o código e tente de novo")
        pergunta1 = input("Código está executando?")
    if pergunta1 =='s':
        pegunta2  = input("Produz o resultado correto?")
        if pergunta2 == "n":
            print ("Corrija o código e tente de novo")
            pergunta1 = "n"
        elif pergunta2 == "s":
            t = False
print ('Parabéns'):

       