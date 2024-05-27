import numpy as np
import matplotlib.pyplot as plt

# 定义函数 / Определение функции
def y(x):
    return np.arccos(2 * x)

# 定义区间和步长 / Определение интервала и шага
x_values = np.arange(0, 0.5 + 0.06, 0.06)
y_values = y(x_values)

# 创建阶梯图 / Создание ступенчатого графика
plt.figure(figsize=(10, 6))
plt.step(x_values, y_values, where='mid', color='maroon', linestyle='-', marker='<', markersize=8, markerfacecolor='maroon', markeredgewidth=2)

# 定制图形 / Настройка графика
plt.title(r'Stair-step plot of $y(x) = \arccos(2x)$')  # 添加标题 / Добавление заголовка
plt.xlabel('x')  # 设置 x 轴标签 / Установка метки оси x
plt.ylabel('y(x)')  # 设置 y 轴标签 / Установка метки оси y
plt.grid(True)  # 添加网格 / Добавление сетки

# 显示图形 / Отображение графика
plt.show()
