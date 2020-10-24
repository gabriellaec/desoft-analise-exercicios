yesno=input(print("Está funcionando?"))

if (yesno == "sim"):
    print("Sem problemas!")
else:
    yesno = input(print("Você consegue consertar?"))

if (yesno == "sim"):
    print("Sem problemas")
else:
    yesno=(input(print("Você precisa consertar?")))
    
if (yesno == "nao" or "não"):
    print("Sem problemas!")
else:
    print("Apague tudo e tente novamente")
