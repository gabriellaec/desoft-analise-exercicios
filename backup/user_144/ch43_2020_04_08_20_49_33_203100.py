lista = ["JANEIRO","FEVEREIRO","MARÇO","ABRIL","MAIO","JUNHO","JULHO"
         ,"AGOSTO","SETEMBRO","OUTUBRO","NOVEMBRO","DEZEMBRO"]

        
numero = int(input("Digite um número: "))
for i in range(len(lista)):
    if numero == i+1:
        print(lista[i])