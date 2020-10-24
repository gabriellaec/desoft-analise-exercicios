nome = input("Qual o nome do seu usuário?")

if "Chris" or "chris" in nome:
	print("Todo mundo odeia o Chris")
else:
	print("Olá, {}".format(nome))