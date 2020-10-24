senha = "desisto"
a = input("Qual a senha?")
while a != senha:
    a = input("Qual a senha?")
    print ("Errou")
if a == senha:
        print("Você acertou a senha!")