class Retangle:
    def __init__ (self,vx,vy):
        self.x = vx
        self.y = vy
        
    def calcula_perimetro (self, outroPonto):
        XDelta = abs(self.x - outroPonto.x)
        YDelta = abs(self.y - outroPonto.y)
        return (2*XDelta)+ (2*YDelta)
    
    def calcula_area (self, outroPonto):
        XDelta = abs(self.x - outroPonto.x)
        YDelta = abs(self.y - outroPonto.y)
        return XDelta * YDelta