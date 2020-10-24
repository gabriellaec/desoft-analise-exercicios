Senha = True
resposta = input("Qual é a senha")
while Senha:
	if resposta=="desisto":
		Senha = False
	else:
		Senha = True
	return resposta
print("Você acertou a senha!")