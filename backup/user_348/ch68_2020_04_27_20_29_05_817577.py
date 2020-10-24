def separa_trios (lista):
    trio = []
    i = 0
    while i < len(lista):
        alunos = lista[i:2]
        trio.append(alunos)
        i = i + 3
    return trio

print(separa_trios (['A0', 'A1', 'A2'])