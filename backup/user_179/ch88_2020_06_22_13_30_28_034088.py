class Retangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def calcula_perimetro(self,ps.x,ps.y):
        dx = ps.x - self.x    
        dy = ps.y - self.y 
        return (dx*2 + dy*2)
    def calcula_area(self,ps.x,ps.y):
        dx = ps.x - self.x    
        dy = ps.y - self.y 
        return (dx*dy)