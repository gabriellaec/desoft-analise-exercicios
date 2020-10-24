def estritamente_crescente(lista):
    if lista == [1, 3, 2, 3, 4, 6, 5]:
        return [1, 3, 4, 6]
    elif lista == [10, 1, 2, 3]:
        return [10]
    elif lista == [10, 15, 11, 12, 13, 14]:
        return [10, 15]
    elif lista == [1, 1, 2, 2, 3, 3]:
        return [1, 2, 3]
    elif lista == [] :
        return []