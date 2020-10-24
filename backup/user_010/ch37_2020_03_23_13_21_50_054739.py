invalida = True
senha = "desisto"
while invalida:
    resp = str(input("Qual é a senha?"))
    if resp == senha:
        print ("Você acertou a senha!")
        invalida = False
    else:
        print ("Senha inválida.")