Senha = False
resposta = input("Qual é a senha")
while Senha:
	if resposta=="desisto":
		Senha=True
	else:
		print("tenta denovo")
		
print("Você acertou a senha!")