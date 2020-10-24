class Retangulo:
    def calcula_perimetro(self, inferior_esquerdo, superior_direito):
        self.x = 2 * (superior_direito.x - inferior_esquerdo.x)
        self.y = 2 * (superior_direito.y - inferior_esquerdo.y)
        perimetro = self.y + self.x
    
    def __init__(self, inferior_esquerdo, superior_direito):
        self.x = superior_direito.x - inferior_esquerdo.x
        self.y = superior_direito.y - inferior_esquerdo.y
        area = self.x * self.y