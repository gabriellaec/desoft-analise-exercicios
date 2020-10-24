senha=True

i=0
while senha:
    x=input("Qual a senha?")
    if x=="desisto":
        print("Você acertou a senha!")
        senha=False
    else:
        print("Errou! :(")
        senha=True
    i+=1
        