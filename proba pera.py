import matplotlib.pyplot as plt
from datetime import datetime

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
graph_plotter = ScalableGraphPlotter()
graph_plotter.add_data_point(10.5, "2023-09-14 10:00:00")
graph_plotter.add_data_point(15.2, "2023-09-14 10:15:00")
graph_plotter.add_data_point(8.7, "2023-09-14 10:30:00")
graph_plotter.set_scale_factor(2.0)  # Увеличим масштаб в два раза
graph_plotter.plot_graph()