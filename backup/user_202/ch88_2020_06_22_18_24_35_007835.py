point = Ponto(x,y)
class Retangulo():
    def __init__(self,point):
        baixo = point(x,y)
        alto = point(x,y)
    def calcula_perimetro(self):
        perimetro = 0
        perimetro += 2*(alto.y-baixo.y)
        perimetro += 2*(alto.x-baixo.x)
        return perimetro
    def calcula_area(self):
        area = 0
        y = alto.y-baixo.y
        x = alto.x-baixo.x
        area = x*y
        return area
        
        