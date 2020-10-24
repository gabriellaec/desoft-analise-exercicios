class retangulo:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def calcula_perimetro(self):
        perimetro=((self.x)*2)+((self.y)*2)
        return perimetro
    def calcula_area(self):
        area=(self.x)*(self.y)
        return area