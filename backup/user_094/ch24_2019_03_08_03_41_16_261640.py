def classifica_triangulo(ladoa,ladob,ladoc):
    if ladoa == ladob and ladoa == ladoc:
        return "equilátero"
    elif ladoa!=ladob and ladoa!=ladoc and ladob!=ladoc:
        return "escaleno"
    else:
        return "isóceles"