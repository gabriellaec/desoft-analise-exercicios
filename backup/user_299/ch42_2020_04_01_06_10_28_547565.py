i=0
sem_fim=True
lista = ['lista com palavras do usuário']
palavras_com_a_no_cmc = []
while i<len(lista) and sem_fim:
    palavra = input("Digite uma palavra:")
    lista.append(palavra)
    primeira_letra = palavra[0]
    if palavra == "fim" or palavra == "Fim":
        sem_fim=False
        i=len(lista)
    elif primeira_letra == "a" or primeira_letra == "A":
        palavras_com_a_no_cmc.append(palavra)
        i=i+1
        print(palavras_com_a_no_cmc[i])