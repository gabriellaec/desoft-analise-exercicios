def mais_frequente(lista2):
    ocorrencias=conta_ocorrencias(lista2)
    maior_ocorrencia=0
    palavra_mais_frequente=''
    for palavra,numero_ocorrencias in ocorrencias.items():
        if numero_ocorrencias > maior_ocorrencia :
            maior_ocorrencia=numero_ocorrencias
            palavra_mais_frequente= palavra
    return palavra_mais_frequente