class Retangulo:
    def __init__ (self,a,b):
        self.ax=a*x
        self.bx=b*x
        self.ay=a*y
        self.by=b*y
    def calcula_perimetro(self):
        ladoX=self(self.bx-self.ax)*2
        ladoy=self(self.by-self.ay)*2
        perimetro=ladoX+ladoY
        return perimetro
    def calcula_area(self):
        ladoX=(self.bx-self.ax)
        ladoY=(self.by-self.ay)
        area=ladoX*ladoY
        return area
        
        
   
        
    