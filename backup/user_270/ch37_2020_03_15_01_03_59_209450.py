senha_py = "desisto"
t = True
while t :
    senha_user = input("Chute uma senha: ")
    if senha_user != senha_py:
        print("Você errou!! Tente chutar novamente.")
    else:
        t = False
print("Você acertou a senha!")