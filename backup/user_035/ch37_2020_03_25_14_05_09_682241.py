Senha = True
resposta = input("Qual é a senha")
while Senha:
	if resposta!="desisto":
		Senha = True
        return resposta
	else:
		Senha = False
print("Você acertou a senha!")