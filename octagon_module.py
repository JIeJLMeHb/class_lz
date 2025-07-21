import numpy as np
import matplotlib.pyplot as plt

class Octagon:
    def __init__(self, side_length):
        self.side_length = side_length
        self.corner = 135 # Угол между сторонами
        self.CONSTANT = 1 + np.sqrt(2)
        print("Создание объекта Octagon")

    def get_radius_opis(self):
        return self.side_length / (2 * np.sin(np.pi / 8))
    
    def get_radius_vpis(self):
        return (self.side_length * (1 + np.sqrt(2))) / 2
    
    def print_flush(self):
        angles = np.linspace(0, 2 * np.pi, 9)[:-1] # 8 точек (0° до 360°)
        R_opis = self.get_radius_opis()
        R_vpis = self.get_radius_vpis()
        
        x_oct = R_opis * np.cos(angles) # Координаты вершин
        y_oct = R_opis * np.sin(angles)
        x_oct = np.append(x_oct, x_oct[0]) # Замыкание точек
        y_oct = np.append(y_oct, y_oct[0])

        plt.figure(figsize=(10, 10)) # График

        plt.gca().add_patch(
            plt.Circle((0, 0), R_opis, color='red', fill=False, linestyle='--', 
                      label=f'Описанная (R={R_opis:.2f})')
        )

        plt.gca().add_patch(
            plt.Circle((0, 0), R_vpis, color='green', fill=False, linestyle=':', 
                      label=f'Вписанная (R={R_vpis:.2f})')
        )

        plt.plot(x_oct, y_oct, 'b-', linewidth=2, label='Восьмиугольник')

        plt.axis('equal')
        plt.title(f"Правильный восьмиугольник (сторона = {self.side_length})")
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.legend()
        plt.show()
