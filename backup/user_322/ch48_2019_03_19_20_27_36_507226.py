meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
escolha = (input("escolha um mes:"))
i = 0
while i < 11:
    if meses[i] == escolha:
        a = i
        i = i + 1
    else: 
        i = i + 1
print(a)