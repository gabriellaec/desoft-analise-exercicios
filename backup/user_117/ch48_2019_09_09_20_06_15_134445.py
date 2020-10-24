m = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
mes = input("nome do mês? ")

i = 0
while i < len(m):
    if mes == m[i]:        
        print(i+1)
    i+=1