nome_do_mes =  (input("Qual é o nome do mes? "))

lista = [0, "janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
t = 0
while t < len(lista):
    if nome_do_mes == lista[t]:
        print(t)
    t += 1