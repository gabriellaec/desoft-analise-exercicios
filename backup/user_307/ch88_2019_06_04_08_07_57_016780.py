class Retangulo():
    
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def calcula_perimetro(self):
        return ((self.b.x-self.a.x)*2)+((self.b.y-self.a.y)*2)
    
    def calcula_area(self):
        return (self.b.x-self.a.x)*(self.b.y-self.a.y)