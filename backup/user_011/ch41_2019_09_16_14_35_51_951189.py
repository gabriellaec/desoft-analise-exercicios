palavra = input("Qual a senha? ")
senha = "desisto"
while palavra != senha:
    palavra = input("Qual a senha? ")
    if palavra == senha:
        print("Você acertou a senha!")