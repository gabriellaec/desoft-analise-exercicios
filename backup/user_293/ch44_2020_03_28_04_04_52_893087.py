meses = ["","Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]

nome = input("Digite o mes: ")

i = 0
while i < len(meses):
    if meses[i] == nome:
        print(i)
    i += 1