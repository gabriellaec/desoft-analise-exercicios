lista_mes = ["janeiro", "fevereiro", "março", "abril", "maio",
             "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
a = (input("Mes:"))


i = 0
while i < len(lista_mes):
    if lista_mes[i] == str(a):
        print(i+1)
        break
    else:
        i += 1
        continue
