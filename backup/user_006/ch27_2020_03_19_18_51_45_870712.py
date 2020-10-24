tem_duvidas= True
while tem_duvidas:
    resposta_do_aluno = input("Voce tem duvida?")
    if resposta_do_aluno!="não":
        print("Pratique mais")
    else:
        tem_duvidas=False
        print("Até a proxima")