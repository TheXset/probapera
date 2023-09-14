import matplotlib.pyplot as plt
from datetime import datetime
import random

class ScalableGraphPlotter:
    def __init__(self):
        self.x = []
        self.y = []
        self.timestamps = []
        self.scale_factor = 1.0  # Исходный масштаб графика

    def add_data_point(self, value, timestamp_str):
        try:
            timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
            self.timestamps.append(timestamp)
            self.x.append(value)
        except ValueError:
            print("Некорректный формат времени. Используйте формат '%Y-%m-%d %H:%M:%S'.")

    def set_scale_factor(self, scale_factor):
        self.scale_factor = scale_factor

    def plot_graph(self):
        plt.figure(figsize=(10, 6))
        scaled_x = [x * self.scale_factor for x in self.x]
        plt.plot(self.timestamps, scaled_x, marker='o', linestyle='-')
        plt.xlabel('Время')
        plt.ylabel('Значение')
        plt.title('Масштабируемый график')
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

# Пример использования:
def main():
    graph_plotter = ScalableGraphPlotter()
    time_step =15
    time_h = 10
    time_m = 0
    for point in range (0,20): #тут можешь поиграться с кол-вом точек
        if time_m == 60:
            time_h+=1
            time_m = 0
            graph_plotter.add_data_point(random.randint(0,256),
                                         f"2023-09-14 {time_h}:{time_m}:00")
        else:
            graph_plotter.add_data_point(random.randint(0,256),
                                        f"2023-09-14 {time_h}:{time_m}:00")
            time_m+=time_step

    graph_plotter.set_scale_factor(2.0)  # Увеличим масштаб в два раза
    graph_plotter.plot_graph()

if __name__ == "__main__":
    main()
