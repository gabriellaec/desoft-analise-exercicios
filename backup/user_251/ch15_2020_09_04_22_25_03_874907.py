Chris = True
def todo_mundo(nome):
    if nome == "Chris":
        return "Todo mundo odeia o chris"
    else:
        return "olá,{0}".format(nome)

nome = str(input("Qual é o seu nome? "))

print(todo_mundo(nome))


