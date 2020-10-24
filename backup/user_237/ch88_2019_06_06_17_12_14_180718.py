class Retangulo:
    def __init__(self, ponto1, ponto2):
        self.canto_inferior_esquerdo = ponto1
        self.canto_superior_direito = ponto2
    
    def calcula_perimetro(self):
        self.perimetro = 2*((canto_superior_direito.y - canto_inferior_esquerdo.y) + (canto_superior_direito.x - canto_inferior_esquerdo.x))
        
    def calcula_area(self):
        self.area = (canto_superior_direito.x - canto_inferior_esquerdo.x) * (canto_superior_direito.y - canto_inferior_esquerdo.y)
    