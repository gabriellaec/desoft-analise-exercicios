class Retangulo:
    def __init__(self, p1, p2):
        self.Ie = p1
        self.Sd = p2
    
    def calcula_perimetro(self):
        perimetro =2*((Retangulo.Ie).x-(Retangulo.Sd).x)+2*((Retangulo.Ie).y-(Retangulo.Sd))
        return perimetro
    def calcula_area(self):
        area = (Ponto_do_canto_inferior_esquerdo.x-Ponto_do_canto_superior_direito.x)*(Ponto_do_canto_inferior_esquerdo.y-Ponto_do_canto_superior_direito.y)
        return area