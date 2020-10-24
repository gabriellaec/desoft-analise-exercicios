senha_py = "desisto"
t = False
while t :
    senha_user = input("Chute uma senha: ")
    if senha_user != senha_py:
        print("Você errou!! Tente chutar novamente.")
    else:
        t = True
print("Você acertou a senha!")