class Retangulo:
    def __init__(self, p1, p2):
        self.infesq_x = p1.x
        self.infesq_y = p1.y
        self.supdir_x = p2.x
        self.supdir_y = p2.y
        
    def calcula_perimetro(self):
        perimetro = 2 * (self.supdir_x - self.infesq_x + self.supdir_y - self.infesq_y)
        return perimetro
    
    def calcula_area(self):
        area = (self.supdir_x - self.infesq_x) * (self.supdir_y - self.infesq_y)
        return area