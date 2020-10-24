lista_mes = ["janeiro","fevereiro","marco","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
a = str(input("Digite o nome de um mes:"))
i = 0
while i<len(lista_mes):
    if lista_mes[i] == a:
        print(i+1)   
    i+=1
    