def remove_vogais(p):
    lista_vogais=['a','e','i','o','u']
    sem_vogal=''
    for i in range(len(p)):
        if p[i] not in lista_vogais:
            sem_vogal+=p[i]
    return sem_vogal
