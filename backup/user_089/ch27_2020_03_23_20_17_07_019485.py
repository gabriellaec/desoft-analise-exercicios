ter_duvidas= True
a= input("Você tem duvidas na disciplina?")
while a != "não":
    print("Pratique mais")
    a= input("Você tem duvidas na disciplina?")
    ter_duvidas=True
else:
    ter_duvidas=False
    print("Até a proxima")