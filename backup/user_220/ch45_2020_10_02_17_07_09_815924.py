j = True
lista = []
t=0
while j:
    pergunta = int(input("Digite um número inteiro positivo: "))
    if pergunta > 0:
        lista.append(pergunta)
        t+=1
    else:
        j = False

def reverse(lista):
    lista.reverse()
    return lista

print(reverse(lista))