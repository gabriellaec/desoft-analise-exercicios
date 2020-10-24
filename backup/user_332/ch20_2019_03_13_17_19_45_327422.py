def pergunta_nome (NOME):
	if (NOME == "Chris"):
    	return("Todo mundo odeia o Chris")
	else:
    	return("Ola, {}".format(NOME))
        
NOME = input("Qual eh seu nome?")

print(pergunta_nome(NOME))