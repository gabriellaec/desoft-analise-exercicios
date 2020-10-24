dicionario = {"a": "b", "c": "b", "b": "a"}
lista = []
lista2 = []

def simplifica_dict(dicionario):
    for chave, valor in dicionario.items():
        j = [chave, valor]
        lista.append(j)
    for i in lista:
        if i not in lista2:
            lista2.append(i)
        return lista2
    print(lista2)

print(simplifica_dict(dicionario))