class Retangulo:
    def __init__(self, p1, p2):
        self.Ponto_do_canto_inferior_esquerdo = p1
        self.Ponto_do_canto_superior_direito = p2
    
    def calcula_perimetro(self):
        perimetro = 2*(p1.x-p2.x) + 2*(p1.y-p2.y)
        return perimetro
    def calcula_area(self):
        area = (inferior_esquerdo.x-superior_direito.x)*(inferior_esquerdo.y-superior_direito.y)
        return area