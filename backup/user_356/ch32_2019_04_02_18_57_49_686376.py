a=input("Tem dúvidas na disciplina?: ")
duvidas=True
while duvidas:
    if a!="não":
        print("Pratique mais")
        a=input("Ainda tem dúvidas?: ")
    if a=="não":
        duvidas=False
        print("Até a próxima")