duvida=True
resp=str(input("Tem dúvidas? Reponda sim/não"))
while duvida:
    if resp!="não":
        print("Pratique mais")
    else: 
        print("Até a próxima")
        resp=str(input("Tem dúvidas? Reponda sim/não"))
       