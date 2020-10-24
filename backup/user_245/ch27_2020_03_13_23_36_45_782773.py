resp_aluno = True
while resp_aluno == True:
    print("Pratique mais")
    resp_d_aluno = str(input("Você tem mais dúvidas? "))
    if resp_d_aluno != "não":
        resp_aluno = False
        print ("Até a próxima")