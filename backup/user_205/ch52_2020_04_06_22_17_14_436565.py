def calcula_total_da_nota(lista1,lista2):
    soma=0
    for i in range(len(lista1)):
        for i in range(len(lista2)):
            soma = soma + lista1[i]*lista2[i]

        return (soma)
   