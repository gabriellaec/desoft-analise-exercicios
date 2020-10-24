from typing import List
def junta_nomes(lista1: List[str], lista2: List[str], lista3: List[str]) -> List[str]:
    lista_de_nomes_completos = []
    for sobrenome in lista3:
        for nome in lista1 + lista2:
            lista_de_nomes_completos.append(f"{nome} {sobrenome}")
    return lista_de_nomes_completos