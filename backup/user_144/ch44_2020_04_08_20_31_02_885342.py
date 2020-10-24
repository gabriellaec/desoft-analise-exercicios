
lista = ["JANEIRO","FEVEREIRO","MARÇO","ABRIL","MAIO","JUNHO","JULHO"
         ,"AGOSTO","SETEMBRO","OUTUBRO""NOVEMBRO","DEZEMBRO"]

mes = input("Digite o mês: ")
for i in lista:
    if mes == i:
       
        print(f"{mes} é o mês de número {lista[i]}")