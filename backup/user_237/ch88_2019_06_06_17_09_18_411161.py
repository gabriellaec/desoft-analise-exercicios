class Retangulo:
    def __init__(self, ponto1, ponto2):
        self.canto_inferior_esquerdo = ponto1
        self.canto_superior_direito = ponto2
    
    def calcula_perimetro(self):
        self.perimetro = 2*((ponto2.y - ponto1.y) + (ponto2.x - ponto1.x))
        
    def calcula_area(self):
        self.area = (ponto2.x - ponto1.x) * (ponto2.y - ponto1.y)
    