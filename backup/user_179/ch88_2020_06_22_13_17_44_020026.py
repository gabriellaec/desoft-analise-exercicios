class Retangulo:
    dx = ps.x - self.x    
    dy = ps.y - self.y 
    def calcula_perimetro(self,ps):
        return (dx*2 + dy*2)
    def calcula_area(self):
        return (dx*dy)