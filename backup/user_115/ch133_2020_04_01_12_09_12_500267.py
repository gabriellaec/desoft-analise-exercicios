yesno=input(print("Está funcionando?"))

if (yesno == "sim"):
    print("Sem problemas!")
else:
    yesno = input(print("Você consegue consertar?"))

if (yesno == "sim"):
    print("Sem problemas")
else:
    yesno=(input(print("Você precisa consertar?")))
    
if (yesno == "sim"):
    print("Apague tudo e tente novamente!")
else:
    print("Sem problemas!")
