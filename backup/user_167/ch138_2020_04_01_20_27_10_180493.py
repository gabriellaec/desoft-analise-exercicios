a=input("Código está executando?:")
while a != "s":
    a=input("Código está executando?:")
    if a == "n":
        print ("Corrija o código e tente de novo")
   
    if a == "s":
        b=input("o codigo produz o resultado correto?:")
        if b== "n":
            print("Corrija o código e tente de novo e volte para o começo de tudo")
            break
        else:
             print("Parabéns!")
        
         

    

    