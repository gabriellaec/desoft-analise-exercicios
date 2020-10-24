a = input("Qual o nome do mês?(Utilize letra minuscula):")

m = ["janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]

i = 1

while i <= 12:
    if m[i] == a:
        print(i)
    i+=1
