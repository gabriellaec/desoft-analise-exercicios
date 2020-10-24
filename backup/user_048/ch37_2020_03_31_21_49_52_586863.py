senha=False
x=input("Qual e a senha?")
if x!="desisto":
    senha=True
while senha==True:
    x=input("Qual e a senha?")
    if x!="desisto":
        senha=True
    else:
        senha=False
print("Você acertou a senha!")