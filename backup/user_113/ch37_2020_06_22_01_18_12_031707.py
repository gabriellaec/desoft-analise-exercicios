x= True

while x==True:
    senha = input ("Teste uma palavra: ")
    if senha != "desisto": 
        x=True
    elif senha == "desisto":
        print ("Você acertou a senha!")
        x=False