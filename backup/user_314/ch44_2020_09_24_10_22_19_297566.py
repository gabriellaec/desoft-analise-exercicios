nome= input("Nome do mês: ")

lista_meses=["janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","Novembro","Dezembro"]

for i in range(len(lista_meses)):
    if(lista_meses[i]== nome):
        print(i+1)
