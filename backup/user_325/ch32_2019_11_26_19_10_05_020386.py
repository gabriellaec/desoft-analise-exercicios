tem_duvidas = True

while tem_duvidas:
    duvida = str(input("tem duvidas na disciplina? "))
    if duvida != "não":
        print("Pratique mais")
    else:
        tem_duvidas = False
print("Até a próxima")