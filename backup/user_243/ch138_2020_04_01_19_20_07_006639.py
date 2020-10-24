z= True
while z:
    a=input("Código está executando?(s/n)")
    if a!="s":
        print("Corrija o código e tente de novo")
        a=input("Código está executando?(s/n)")
    elif a=="s":
        b=input("O código produz o resultado correto(s/n)") 
        if b=="n":
                print ("Corrija o código e tente de novo e volte para o começo de tudo")
        else:
            print("Parabéns!")
            