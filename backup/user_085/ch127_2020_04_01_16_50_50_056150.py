def calcula_elongacao(A, f, w, t):
    import math
    return A* math.cos(math.degrees(f) + math.degrees(w)*t)