def QualMes(numero):
    lista = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
    mes = 0
    mes = lista[numero-1]
    return mes

n = int(input("Digite um número para descobrir o mês equivalente: "))
while n<1 or n>12:
    n = int(input("Digite um número para descobrir o mês equivalente: "))
print (QualMes(n))