class Retangulo:
    def __init__(self, p1, p2):
        self.inferior_esquerdo = p1
        self.superior_direito = p2
    
    def calcula_perimetro(self):
        perimetro = 2*(inferior_esquerdo.x-superior_direito.x) + 2*(inferior_esquerdo.y-superior_direito.y)
        return perimetro
    def calcula_area(self):
        area = (inferior_esquerdo.x-superior_direito.x)*(inferior_esquerdo.y-superior_direito.y)
        return area