pergunta_nome = input("Qual o seu nome?");

a = str(pergunta_nome);

if a == "Chris":
    print("Todo mundo odeia o Chris");
else:
    print("Olá, {0}". format(pergunta_nome));