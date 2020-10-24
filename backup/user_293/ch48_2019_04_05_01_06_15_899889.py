meses_nome = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
meses = [1,2,3,4,5,6,7,8,9,10,11,12]
n = input("Digite o nome do mes: ")
while n != meses_nome
    print("Inválido")
    n = input("Digite o nome do mes: ")
print(meses[n])
