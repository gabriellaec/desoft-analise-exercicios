senha = "desisto"
tentativa = str(input("Tente acertar a senha"))

while tentativa != senha:
    tentativa = str(input("Tente acertar a senha"))
    
print("Você acertou a senha!")