comp = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
mes = input("Digite um mês. ")
x=""
num=0
i=0
       
while x!= mes:
    if comp[i]== mes:
        x=mes
        num=i
    i=i+1

print(num+1)