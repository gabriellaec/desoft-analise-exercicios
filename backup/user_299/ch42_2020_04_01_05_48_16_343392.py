i=0
sem_fim=True
lista = ['lista','com','palavras','do','usuário']
while i<len(lista) and sem_fim:
    lista[i] = input("Digite uma palavra:")
    palavra = lista[i]
    lista.append(palavra)
    primeira_letra = palavra[1]
    if palavra == "fim" or palavra == "Fim":
        sem_fim=False
        i=len(lista)
    elif primeira_letra == "a" or primeira_letra == "A":

        palavras_com_a_no_cmc.append(lista[i])
        i=i+1
    
print(palavras_com_a_no_cmc)
