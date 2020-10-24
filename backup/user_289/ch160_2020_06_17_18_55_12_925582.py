from math import*
lista_diferencas = []
for grau in range(0, 91):
    seno_bhaskara = (4*grau*(180-grau))/(40500 - grau*(180 - grau)) 
    seno_python = sin(radians(grau))
    diferenca = abs(seno_python - seno_bhaskara)
    lista_diferencas.append(diferenca)
termo = max(lista_diferencas)
valor = lista_diferencas.index(termo)
print(valor)