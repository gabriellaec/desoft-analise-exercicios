def pergunta_nome (NOME):
	if (NOME == "Chris"):
    	print("Todo mundo odeia o Chris")
	else:
    	print("Ola, {}".format(NOME))
        
NOME = input("Qual eh seu nome?")

print(pergunta_nome(NOME))