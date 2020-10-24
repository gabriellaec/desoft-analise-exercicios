a = input("Nome do mes: ")
lista = ["janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
i = 0
while i < len(lista):
    if a == lista[i]:
        print (i+1)
    i +=1