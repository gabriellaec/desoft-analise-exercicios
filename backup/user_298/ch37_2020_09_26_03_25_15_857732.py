tentando = True
while tentando:
    senha = input("Tente a senha: ")
    if senha == "desisto":
        tentando = False 
        print("Você acertou a senha!")