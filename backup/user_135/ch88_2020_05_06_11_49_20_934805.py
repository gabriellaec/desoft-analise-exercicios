class Retangulo:
    def __init__(self, inferior_esquerdo, superior_direito):
        self.inferior_esquerdo = inferior_esquerdo
        self.superior_direito = superior_direito

    def calcula_perimetro(self):
        lado_x = superior_direito.x - inferior_esquerdo.x
        lado_y = superior_direito.y - inferior_esquerdo.y
        perimetro = lado_x * 2 + lado_y * 2
        return perimetro
    
    def calcula_area(self):
        lado_x = superior_direito.x - inferior_esquerdo.x
        lado_y = superior_direito.y - inferior_esquerdo.y
        area = lado_x * lado_y
        return area