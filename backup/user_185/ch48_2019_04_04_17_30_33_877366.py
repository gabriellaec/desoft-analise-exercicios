nome_do_mês = input("Digite o nomê do mês: ")
index = 0
lista = ["","janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
while index < len(lista):
    if lista[index] != nome_do_mês:
        index = index + 1
    else:
        break
print(index)
    