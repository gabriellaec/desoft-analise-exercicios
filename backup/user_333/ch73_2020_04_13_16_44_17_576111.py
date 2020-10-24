def remove_vogais(palavra):
    lista_vogais=['a','e','i','o','u']
    sem_vogal=''
    for i in range(len(palavra)):
        if palavra[i] not in lista_vogais:
            sem_vogal.append(palavra[i])
    return sem_vogal