duvida=True
resp=str(input("Tem dúvidas? Reponda s/n"))
while duvida:
    if resp=="n":
        duvida=False
        print("Até a próxima")
    else: 
        print("Pratique mais")
        resp=str(input("Tem dúvidas? Reponda s/n"))
       