i=0
nome = input("Digite o mês: ")
mes = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
while i<12:
    if nome == mes[i]:
        print(i+1)
        i = 12
    else:
        i+=1