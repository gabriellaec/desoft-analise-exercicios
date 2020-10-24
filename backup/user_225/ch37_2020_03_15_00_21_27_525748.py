oi = True
while oi:
    senhadousuario = input("Qual é a senha? ")
    if senhadousuario != "desisto":
        oi = True
    else: 
        oi=False
print ("Você acertou a senha!")