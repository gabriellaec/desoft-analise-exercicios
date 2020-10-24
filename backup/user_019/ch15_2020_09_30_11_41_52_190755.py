usuario = str(input("Qual o seu nome? "))
if usuario == "Chris":
    return ("Todo mundo odeia o Chris")
else:
    return ("Olá, {0}".format(usuario))