def nobody_likes_chris(nome):
    if nome=="Chris":
        return ("Todo mundo odeia o Chris")
    else:
        return ("Olá, {0}".format(nome))

nome= str(input("Qual é o seu nome?: "))
print(nobody_likes_chris(nome))