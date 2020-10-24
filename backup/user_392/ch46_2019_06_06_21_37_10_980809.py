palavra = input('digite uma palavra, e fim para terminar:')
fim = 'fim'
lista = []

while palavra != fim:
    lista.append(palavra)
    palavra = input('digite umaoutra palavra, e fim para terminar')

i = 0
lista_real = []
while i < len(lista):
    lista_de_a = lista[i]
    letra = lista_de_a[0]
    if letra == 'a':
        lista_real.append(lista_de_a)
    i += 1
print(lista_de_a)
        
        