class Retangulo:
    def __init__ (self, inferior_esquerdo, superior_direito):
        self.inferior_esquerdo = inferior_esquerdo
        self.superior_direito = superior_direito
    
    def calcula_perimetro(self):
        x = self.inferior_esquerdo.x
        y = self.superior_direito.y
        a = self.inferior_esquerdo.a
        b = self.superior_direito.b
        
        dx = a - x
        dy = b - y
        
        return (2*dx + 2*dy)
    def calcula_area(self):
        x = self.inferior_esquerdo.x
        y = self.superior_direito.y
        a = self.inferior_esquerdo.a
        b = self.superior_direito.b
        
        dx = a - x
        dy = b - y
        
        return (dx*dy)