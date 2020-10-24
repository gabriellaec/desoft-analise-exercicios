j=True
while j==True:
    x=input(str("Qual palavra é a senha?"))
    if x!=('desisto'):
        print ("tente novamente")
        j=True
    else:
        print("Você acertou a senha!")
        j=False