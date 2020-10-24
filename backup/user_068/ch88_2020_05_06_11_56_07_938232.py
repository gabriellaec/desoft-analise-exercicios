
class Retangulo:
    def __init__(self, inferior_esquerdo, superior_direito):
        self.inferior_esquerdo = inferior_esquerdo
        self.superior_direito = superior_direito
        
    def calcula_perimetro(self):
        x = self.inferior_esquerdo.x
        y = self.inferior_esquerdo.y
        a = self.superior_direito.x
        b = self.superior_direito.y
        
        dx = a - x
        dy  = b - y
        
        
        return (2*dx  + 2*dy)
    def calcula_area(self):
        x = self.inferior_esquerdo.x
        y = self.inferior_esquerdo.y
        a = self.superior_direito.x
        b = self.superior_direito.y
        
        dx = a - x
        dy  = b - y
        
        return (dx*dy)
        
        