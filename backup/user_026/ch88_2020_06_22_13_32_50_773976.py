class Retangulo:
    def __init__(self, p1, p2):
        self.ponto_de_baixo_esquerdo= p1
        self.ponto_de_cima_direito= p2
    def d(self): #distancia entre os pontos
        ponto_x= (self.ponto_de_cima_direito.x - self.ponto_de_baixo_esquerdo.x)**2
        ponto_y= (self.ponto_de_cima_direito.y - self.ponto_de_baixo_esquerdo.y)**2
        return (ponto_x + ponto_y)**(1/2)
    def calcula_perimetro(self):
        lado_x= (self.ponto_de_cima_direito.x - self.ponto_de_baixo_esquerdo.x)
        lado_y= (self.ponto_de_cima_direito.y - self.ponto_de_baixo_esquerdo.y)
        return ((lado_x*2) + (lado_y*2))
    def calcula_area(self):
        lado_x= (self.ponto_de_cima_direito.x - self.ponto_de_baixo_esquerdo.x)
        lado_y= (self.ponto_de_cima_direito.y - self.ponto_de_baixo_esquerdo.y)
        return (lado_x * lado_y)