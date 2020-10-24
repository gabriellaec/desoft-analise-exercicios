meses = ["janeiro", "fevereiro", "marco", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
tamanho = len(meses)
pede_mes = input("diga o nome do mes: ")
i = 0
while i < tamanho:
    if meses[i] == pede_mes:
        print(meses[i + 1])
    i += 1
    
   
