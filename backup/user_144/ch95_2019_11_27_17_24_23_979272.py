# Funcao auxiliar para calcular total por estado
def total_estado(dic):
    resultado = {}
    for populacao in dic:
        popu = dic[populacao]
        soma = 0
        for estado in popu:
            valor = popu[estado]
            soma += valor
        resultado[populacao] = soma
    return resultado 

print(total_estado(brasil))

# Funcao de mais populoso       
def mais_populoso(dic):
    total = total_estado(dic)
    maior = 0
    maior_estado = ""
    for populacao in total:
        popu_total = total[populacao]
        if popu_total > maior:
            maior = popu_total
            maior_estado = populacao
    return maior_estado

#Usando o exemplo para teste    
print("O estado mais populoso é {}".format(mais_populoso(brasil)))