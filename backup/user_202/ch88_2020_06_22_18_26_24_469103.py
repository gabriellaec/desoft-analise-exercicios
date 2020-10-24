class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Retangulo():
    def __init__(self,x,y):
        baixo = Ponto(x,y)
        alto = Ponto(x,y)
    def calcula_perimetro(self):
        perimetro = 0
        perimetro += 2*(self.alto.y-self.baixo.y)
        perimetro += 2*(self.alto.x-self.baixo.x)
        return perimetro
    def calcula_area(self):
        area = 0
        y = self.alto.y-self.baixo.y
        x = self.alto.x-self.baixo.x
        area = x*y
        return area
        
        