# Импорт нужных библиотек
import math
import matplotlib.pyplot as plt


# Класс
class Octagon:

    # Конструктор
    def __init__(self, side_length):
        self.side_length = side_length
        self.angle = math.pi / 4  # угол октанога
        self.k = 1 + math.sqrt(2)  # константа k
        
    # Радиус описанной окружности
    def get_radius_circumscribed(self):
        return self.side_length/(2-2**0.5)**0.5

    # Площадь описанной окружности
    def get_area_circumscribed(self):
        radius = self.get_radius_circumscribed()
        return math.pi * (radius ** 2)
    
    # Радиус вписанной окружности
    def get_radius_inscribed(self):
        return self.side_length*0.5*self.k

    # Площадь вписанной окружности
    def get_area_inscribed(self):
        radius1 = self.get_radius_inscribed()
        return math.pi * (radius1 ** 2)

    # Собственная площадь
    def get_area(self):
        return 2 * (1 + math.sqrt(2)) * (self.side_length ** 2)

    # Собственный периметр
    def get_perimeter(self):
        return 8 * self.side_length
    
    # Визуализация
    def draw(self):
        R_out = self.side_length/(2-2**0.5)**0.5  
        R_in = self.side_length*0.5*self.k  
        
        x = [R_out * math.cos(i * self.angle) for i in range(8)]
        y = [R_out * math.sin(i * self.angle) for i in range(8)]
        
        x.append(x[0])  
        y.append(y[0])
        
        fig, ax = plt.subplots(figsize=(6, 6))
    
        ax.plot(x, y, 'bo-', markersize=8, label='Восьмиугольник')
        ax.fill(x, y, alpha=0.3)
        
        circle_out = plt.Circle((0, 0), R_out, color='r', fill=False, linestyle='dashed', label='Описанная окружность')
        ax.add_patch(circle_out)
        
        circle_in = plt.Circle((0, 0), R_in, color='g', fill=False, linestyle='dashed', label='Вписанная окружность')
        ax.add_patch(circle_in)

        ax.axhline(0, color='black', linewidth=0.5)
        ax.axvline(0, color='black', linewidth=0.5)
        ax.grid(True, linestyle='--', linewidth=0.5)
        ax.set_aspect('equal')
        ax.legend()
        plt.xlim(-R_out - 1, R_out + 1)
        plt.ylim(-R_out - 1, R_out + 1)
        plt.show()
    
    # Деструктор
    def __del__(self):
        pass