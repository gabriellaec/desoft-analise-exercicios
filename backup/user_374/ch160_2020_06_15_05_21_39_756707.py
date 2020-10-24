lista = []
contagem = 0

for x in range(0,90):
    sen_x_formula = (4*x*(180-x))/(40500-x*(180-x))
    sen_x_automatico = sin(radians(x))
    lista.append(abs(sen_x_formula) -  sen_x_automatico)

for i in lista:
    if i == max(lista):
        print(contagem)
    else: 
        contagem += 1