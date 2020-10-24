while True:
    perg= input("Código está funcionando?")
    if perg!="n":
        perg2=input("Produz o resultado correto?")
        if perg2!="n":
            print("Parabéns!")
            break
        else:
            print("Corrija o código e tente de novo")
    else:
        print("Corrija o código e tente de novo")
        
        
        