meses = ["","janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]

nome = input("Digite o mes: ")

i = 0
while i < len(meses):
    if nome == meses[i]:
        print(i)
        break
    i += 1