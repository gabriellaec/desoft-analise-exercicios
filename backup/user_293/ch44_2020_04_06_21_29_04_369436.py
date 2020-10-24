meses = ["","janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]

nome = input("Digite o mes: ")

i = 0
for e in meses:
    if nome == e:
        print(i)
    i += 1
    