ano = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
mês = input("Digite o nome do mês: ")
while mês in ano:
    i = 0
    while i < len(ano):
        if ano[i] == mês:
            print("{0}".format(i+1))
            break
        i += 1
    break