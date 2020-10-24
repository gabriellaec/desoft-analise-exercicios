
lista = ["JANEIRO","FEVEREIRO","MARÇO","ABRIL","MAIO","JUNHO","JULHO"
         ,"AGOSTO","SETEMBRO","OUTUBRO""NOVEMBRO","DEZEMBRO"]

for i in lista:
    mes = input("Digite o mês: ")
    if mes == i:
        print(f"{mes} é o mês de número {lista[i]}")