lista = ["JANEIRO","FEVEREIRO","MARÇO","ABRIL","MAIO","JUNHO","JULHO"
         ,"AGOSTO","SETEMBRO","OUTUBRO","NOVEMBRO","DEZEMBRO"]

mes = input("Digite o mês: ").upper()
for i in range(len(lista)):
    if mes == lista[i]:
        print(i)