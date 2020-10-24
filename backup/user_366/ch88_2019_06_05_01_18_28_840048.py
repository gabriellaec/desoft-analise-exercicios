
class Retangulo():
    
    def __init__(self, ponto1, ponto2):
        altura = ponto1.y - ponto2.y
        largura = ponto1.x - ponto2.x
        def calcula_perimetro(self):
            self.perimetro = 2*altura + 2*largura
        def calcula_area(self):
            self.area = altura*largura