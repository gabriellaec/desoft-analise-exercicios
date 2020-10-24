m = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
mes = input("nome do mês?")

i = 0
while i < len(m):
    if mes == m[i]:        
        print(i+1)
    i+=1