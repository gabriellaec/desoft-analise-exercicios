tem_duvida = True
while tem_duvida:
    resposta = input("Alguma Duvida? (s/não): ")
    if resposta != "não":
        print("Pratique mais")
    else:
        tem_duvida = False
print("Até a próxima")
