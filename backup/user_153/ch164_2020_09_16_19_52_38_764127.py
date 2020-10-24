def traduz(lista, dicionario):
    lista_traduzida = [dicionario[word] for word in lista]
    return lista_traduzida

# eng2port = {'pineapple': 'abacaxi', 'plum': 'ameixa', 'blackberry': 'amora', 'apple': 'maçã', 'cashew': 'caju', 'cherry': 'cereja'}
# lista_eng = ['blackberry', 'cherry', 'plum', 'apple', 'pineapple']
# print(traduz(lista_eng, eng2port))