class Retangulo:
    def __init__(self, inferior_esquerdo, superior_direito):
        perimetro_x = 2 * (superior_direito.x - inferior_esquerdo.x)
        perimetro_y = 2 * (superior_direito.y - inferior_esquerdo.y)
        perimetro = perimetro_y + perimetro_x
        return perimetro
    
    def __init__(self, inferior_esquerdo, superior_direito):
        base = superior_direito.x - inferior_esquerdo.x
        altura = superior_direito.y - inferior_esquerdo.y
        area = base * altura
        return area