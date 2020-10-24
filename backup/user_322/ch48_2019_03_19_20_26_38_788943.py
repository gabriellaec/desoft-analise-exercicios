meses = ["janeiro", "fevereiro", "marco", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
escolha = (input("escolha um mes:"))
i = 0
while i < 11:
    if meses[i] == escolha:
        print(i+1)
        i = i + 1
    else: 
        i = i + 1