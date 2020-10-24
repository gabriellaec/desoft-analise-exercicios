class Circulo:
    def __init__(self,centro,raio):
        self.centro_x = centro.x
        self.centro_y = centro.y
        self.raio_ = raio
    def contem(self, ponto):
        self.X = ponto.x
        self.Y = ponto.y
        lista_x_menor = self.centro_x - self.raio_ 
        lista_x_maior = self.centro_x + self.raio_
        lista_x = [lista_x_menor,lista_x_maior]
       
        lista_y_menor = self.centro_y - self.raio_ 
        lista_y_maior = self.centro_y + self.raio_
        lista_y = [lista_y_menor,lista_y_maior]
        
        if lista_x[0] <= self.X >= lista_x[1] and lista_y[0] <= self.Y >= lista_y[1]:
            return True
        else: 
            return False
            
            