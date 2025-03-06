import math
import matplotlib.pyplot as plt

class Octagon:
    def __init__(self, side_length):
        self.side_length = side_length
        self.angle = 135  # угол октанога
        self.k = 1 + math.sqrt(2)  # константа k
        
    def get_radius_circumscribed(self):
        return self.side_length * (math.sqrt(self.k/(self.k - 1)))

    def get_area_circumscribed(self):
        radius = self.get_radius_circumscribed()
        return math.pi * (radius ** 2)
    
    def get_radius_inscribed(self):
        return self.side_length * (self.k/ 2)

    def get_area_inscribed(self):
        radius1 = self.get_radius_inscribed()
        return math.pi * (radius1 ** 2)

    def get_area(self):
        return 2 * (1 + math.sqrt(2)) * (self.side_length ** 2)

    def get_perimeter(self):
        return 8 * self.side_length
    
    def draw(self):
        angles = [i * math.pi / 4 for i in range(8)]  # 8 углов для октагона
        x = [self.side_length * math.cos(angle) for angle in angles]
        y = [self.side_length * math.sin(angle) for angle in angles]
        
        plt.fill(x, y, color='orange', alpha=0.5, label='Octagon')
        
        # Вписанная окружность
        inscribed_radius = self.get_radius_inscribed()
        circle_inscribed = plt.Circle((0, 0), inscribed_radius, color='blue', fill=False, label='Inscribed Circle')
        plt.gca().add_artist(circle_inscribed)
        
        # Описанная окружность
        circumscribed_radius = self.get_radius_circumscribed()
        circle_circumscribed = plt.Circle((0, 0), circumscribed_radius, color='red', fill=False, linestyle='--', label='Circumscribed Circle')
        plt.gca().add_artist(circle_circumscribed)

        plt.xlim(-circumscribed_radius - 1, circumscribed_radius + 1)
        plt.ylim(-circumscribed_radius - 1, circumscribed_radius + 1)
        plt.gca().set_aspect('equal', adjustable='box')
        plt.title('Octagon with Inscribed and Circumscribed Circles')
        plt.legend()
        plt.show()