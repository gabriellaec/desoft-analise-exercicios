meses = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]

n = int(input("Digite o numero de mes(1 - 12): "))
while n < 1 or n > 12:
    print("Invalido")
    n = int(input("Digite o numero de mes(1 - 12): "))
     
nome_do_mes = meses[n-1]
print(nome_do_mes)