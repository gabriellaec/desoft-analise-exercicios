#dicionário inicial 
estados = { 'SP':{'São Paulo':21571281, 'Campinas': 3224443},
            'MG':{'Belo Horizonte': 2893713, 'Uberlândia':611903}}
 
lista = []
i=0
maispop=0
def mais_populoso(dic):
    soma = 0
    estados2= {}
    estados.keys() == estados.keys()
    for k,dic_cidades in dic.items():
        for k,pop in dic_cidades.items():
            soma += pop
        lista.append(soma)

    return lista

def novodic(estados,mais_populoso):
    estados2 = dict 
    estados2.keys() == estados.keys()
    while i<len(estados):
        estados2.values() == lista
    return estados2