lista = ["JANEIRO","FEVEREIRO","MARÇO","ABRIL","MAIO","JUNHO","JULHO"
         ,"AGOSTO","SETEMBRO","OUTUBRO","NOVEMBRO","DEZEMBRO"]

numero = input("Digite um número: ")
for i in range(len(lista)):
    if mes == lista[i]:
        print("Mes {0}, numero: {1}.".format(lista[i],i+1))