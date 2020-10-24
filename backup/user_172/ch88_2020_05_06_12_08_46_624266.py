class Retangulo:
    def _init_(self,coord1, coord2):
        coord1 = Ponto(x1, y1)
        coord2 = Ponto(x2, y2)
        
    def calcula_perimetro(self,x2,y2):
        base = x2 - x1
        altura = y2 - y1
        p = 2*base + 2*altura
        
    def calcula_area(self,x2,y2):
        base = x2 - x1
        altura = y2 - y1
        a = base*altura