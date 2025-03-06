from octagon import Octagon

def main():
    side_length = float(input(f"Введите длину стороны октагона "))  # длина стороны октагона
    octagon = Octagon(side_length)
    
    print(f"Радиус описанной окружности: {octagon.get_radius_circumscribed()}")
    print(f"Площадь описанной окружности: {octagon.get_area_circumscribed()}")
    print(f"Радиус вписанной окружности: {octagon.get_radius_inscribed()}")
    print(f"Площадь вписанной окружности: {octagon.get_area_inscribed()}")
    print(f"Площадь октагона: {octagon.get_area()}")
    print(f"Периметр октагона: {octagon.get_perimeter()}")

    octagon.draw()  # Визуализация

if __name__ == "__main__":
    main()