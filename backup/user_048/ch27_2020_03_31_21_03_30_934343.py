duvida=False
x=input("voce tem duvidas=")
if x !="não":
    duvida=True
while duvida:
    print("Pratique mais")
    input("voce tem duvidas=")
    if x=="não":
        duvida=False
    else:
        duvida=True
print("Até a próxima")