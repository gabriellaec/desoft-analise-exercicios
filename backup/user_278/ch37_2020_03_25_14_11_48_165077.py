senha_errada= True
while senha_errada:
    senha = input("Digite a senha: ")
    if senha!="desisto":
        print ("Senha errada, tente novamente")
    else:
        senha_errada=False
print ("Acertou")