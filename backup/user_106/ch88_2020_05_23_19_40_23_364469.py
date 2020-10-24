class Retangulo:
    def __init__ (self, Ponto(x1, y1), Ponto(x2, y2)):
        u = Ponto(x1, y2)
        d = Ponto(x2, y2)
        t = Ponto(x2, y1)
        q = Ponto(x1, y1)
        
    def calcula_perimetro(self):
        perimetro = (q.y1-d.y2)*2+(d.x2-q.x1)*2
        return perimetro
    def calcula_area(self):
        area=(q.y1-d.y2)*(d.x2-q.x1)
        return area