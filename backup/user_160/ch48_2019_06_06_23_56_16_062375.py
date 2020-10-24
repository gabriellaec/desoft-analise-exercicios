meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
escolha = (input("escolha um mes:"))
i = 0
while i < 12:
    if meses[i] == escolha:
        i = i + 1
        print(i)
    else:
        i = i + 1