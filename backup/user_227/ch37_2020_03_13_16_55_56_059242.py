senha = "desisto"

resposta = input("Adivinhe a senha: ")

while resposta != senha :
    resposta = input("Adivinhe a senha: ")
    
if resposta == senha:
    print("Você acertou a senha!")
