class Retangulo:
    def __init__(self,p1,p2):
        self.ponto_inferior = p1
        self.ponto_superior = p2
        
    def calcula_perimetro(self):
        x1 = self.ponto_inferior.x
        x2 = self.ponto_superior.x
        
        y1 = self.ponto_inferior.y
        y2 = self.ponto_superior.y
        return 2 * (x2-x1) + 2 * (y2-y1)
    
    def calcula_area(self):
        x1 = self.ponto_inferior.x
        x2 = self.ponto_superior.x
        
        y1 = self.ponto_inferior.y
        y2 = self.ponto_superior.y
        return (x2-x1) * (y2-y1)
    