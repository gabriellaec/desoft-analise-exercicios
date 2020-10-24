class Retangulo:
    def __init__(self, ponto1, ponto2):
        self.ponto_inferior_esquerdo= ponto1
        self.ponto_superior_direito= ponto2
    def d(self): #distancia entre os pontos
        x_ponto= (self.ponto_superior_direito.x - self.ponto_inferior_esquerdo.x)**2
        y_ponto= (self.ponto_superior_direito.y - self.ponto_inferior_esquerdo.y)**2
        return (y_ponto + x_ponto)**(1/2)
    def calcula_perimetro(self):
        x_eixo= (self.ponto_superior_direito.x - self.ponto_inferior_esquerdo.x)
        y_eixo= (self.ponto_superior_direito.y - self.ponto_inferior_esquerdo.y)
        return ((x_eixo*2) + (y_eixo*2))
    def calcula_area(self):
        x_eixo= (self.ponto_superior_direito.x - self.ponto_inferior_esquerdo.x)
        y_eixo= (self.ponto_superior_direito.y - self.ponto_inferior_esquerdo.y)
        return (x_eixo * y_eixo)
        