class Retangulo:
    def __init__(self, p1, p2):
        self.Ponto_do_canto_inferior_esquerdo = p1
        self.Ponto_do_canto_superior_direito = p2
    
    def calcula_perimetro(self):
        perimetro = 2*(Ponto_do_canto_inferior_esquerdo.x-Ponto_do_canto_superior_direito.x) + 2*(Ponto_do_canto_inferior_esquerdo.y-Ponto_do_canto_superior_direito.y)
        return perimetro
    def calcula_area(self):
        area = (Ponto_do_canto_inferior_esquerdo.x-Ponto_do_canto_superior_direito.x)*(Ponto_do_canto_inferior_esquerdo.y-Ponto_do_canto_superior_direito.y)
        return area