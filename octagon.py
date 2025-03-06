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
        # Рисуем октаногон
        plt.figure()
        angles = [i * (math.pi / 4) for i in range(8)]
        x = [self.side_length * (math.cos(angle)) for angle in angles]
        y = [self.side_length * (math.sin(angle)) for angle in angles]
        
        # Рисуем октагон
        plt.fill(x, y, color='lightblue', label='Octagon')
        plt.plot(x + [x[0]], y + [y[0]], color='blue')

        # Рисуем описанную окружность
        R = self.get_radius_circumscribed()
        circle_circumscribed = plt.Circle((0, 0), R, color='orange', fill=False, label='Circumscribed Circle')
        plt.gca().add_artist(circle_circumscribed)

        # Рисуем вписанную окружность
        r = self.get_radius_inscribed()
        circle_inscribed = plt.Circle((0, 0), r, color='green', fill=False, label='Inscribed Circle')
        plt.gca().add_artist(circle_inscribed)

        plt.xlim(-R - 1, R + 1)
        plt.ylim(-R - 1, R + 1)
        plt.gca().set_aspect('equal', adjustable='box')
        plt.axhline(0, color='black',linewidth=0.5, ls='--')
        plt.axvline(0, color='black',linewidth=0.5, ls='--')
        plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
        plt.title('Octagon with Circumscribed and Inscribed Circles')
        plt.legend()
        plt.show()