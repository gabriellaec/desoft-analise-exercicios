class Círculo:
    def __init__(self, centro, raio):
        self.centro = centro
        self.raio = raio
        
	def distance_to(self, other_point):
		delta_x = self.centro.x - other_point.x
		delta_y = self.centro.y - other_point.y
		return sqrt(delta_x**2 + delta_y**2)
    
    def pertence(self, ponto):
        return self.centro.distance_to(ponto) <= self.raio