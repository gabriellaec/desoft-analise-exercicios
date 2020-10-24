"""
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
"""
dic = {"janeiro" : 1, "fevereiro": 2, "março": 3, "abril": 4, "maio": 5, "junho": 6, "julho": 7, "agosto": 8, "setembro": 9, "outubro": 10, "novembro": 11, "dezembro": 12}
mes = input("Digite um mês. ")
print(dic[mes])