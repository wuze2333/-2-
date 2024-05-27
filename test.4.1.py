import numpy as np
import matplotlib.pyplot as plt

# 定义函数 / Определение функции
def y(x):
    return 6 * np.cos(5 * x)

# 定义区间和步长 / Определение интервала и шага
x_values = np.arange(0, 2 * np.pi + 0.2, 0.2)
y_values = y(x_values)

# 创建 stem 图 / Создание графика стеблей
plt.figure(figsize=(10, 6))
markerline, stemlines, baseline = plt.stem(x_values, y_values, linefmt='r--', markerfmt='rd', basefmt='k-')

# 设置参数 / Установка параметров
plt.setp(markerline, 'markersize', 8)  # 设置标记大小 / Установка размера маркеров
plt.setp(stemlines, 'linewidth', 1.5)  # 设置线宽 / Установка ширины линий
plt.setp(baseline, 'linewidth', 1)  # 设置基线宽度 / Установка ширины базовой линии

# 定制图形 / Настройка графика
plt.title(r'Stem plot of $y(x) = 6 \cos(5x)$')  # 添加标题 / Добавление заголовка
plt.xlabel('x')  # 设置 x 轴标签 / Установка метки оси x
plt.ylabel('y(x)')  # 设置 y 轴标签 / Установка метки оси y
plt.grid(True)  # 添加网格 / Добавление сетки

# 显示图形 / Отображение графика
plt.show()
