class Retangulo:
    def _init_(self,p1,p2):
        self.p1=p1
        self.p2=p2
        
    def calcula_perimetro(self):
        p= 2*(self.p2.x-self.p1.x)+2*(self.p2.y-self.py.y)
        return p
    
    def calcula_area(self):
        area= (self.x)*(self.y)
        return area