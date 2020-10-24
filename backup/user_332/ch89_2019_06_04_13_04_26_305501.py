class Circulo:
    def __init__(self,x,y):
        self.raio = float(3.14)
        self.centrox = 10
        self.centroy = 10
        def contem(self, ponto):
            
            self.x = ponto.x
            self.y = ponto.y
            if self.x <= 10 + self.raio and self.x >= 10 - self.raio:
                if self.y <= 10 + self.raio and self.y >= 10 - self.raio:
                    return True
            else: 
                return False
        
    