class Retangulo:
    def calcula_perimetro(self,ps):
        dx = ps.x - self.x    
        dy = ps.y - self.y 
        return (dx*2 + dy*2)
    def calcula_area(self,ps):
        dx = ps.x - self.x    
        dy = ps.y - self.y 
        return (dx*dy)