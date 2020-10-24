pergunta= input("Digite um mês: ")
mês_por_extenso= ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

i= 0
while i < 12:
    if pergunta == mês_por_extenso[i]:
        print(i+1)
    i= i + 1 
    