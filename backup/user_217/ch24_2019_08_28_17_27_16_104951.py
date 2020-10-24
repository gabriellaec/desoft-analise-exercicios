def classifica_triangulo(cat1,cat2,hip):
    if cat1==cat2 and cat2==hip and cat1==hip:
        return 'equilátero'
    if cat1!=cat2 or cat2!=hip or cat1!=hip:
        return "isósceles"
    else:
        return "escaleno"