def acerta_senha(palavra):
    if palavra=="desisto":
            return "Você acertou a senha!"
    while palavra != "desisto":
        palavra=str(input("digite uma palavra: "))
        if palavra=="desisto":
            return "Você acertou a senha!"

palavra=str(input("digite uma palavra: "))
print(acerta_senha(palavra))