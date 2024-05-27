import matplotlib.pyplot as plt
import numpy as np

# Определяем функцию, данную на изображении
def f(x):
    return np.cos(x) + (np.sqrt(3)/2)*x - 1/2

# Генерируем значения x
x = np.linspace(-2*np.pi, 2*np.pi, 400)

# Вычисляем значения y
y = f(x)

# Построение графика функции
plt.figure(figsize=(10, 5))
plt.plot(x, y, label='y = cos(x) + (sqrt(3)/2)*x - 1/2')

# Добавление заголовка и подписей с пользовательскими шрифтами
plt.title('График функции: $y = \cos(x) + \\frac{\sqrt{3}}{2}x - \\frac{1}{2}$', fontsize=14, fontweight='bold')
plt.xlabel('Ось X', fontsize=12, color='blue')
plt.ylabel('Ось Y', fontsize=12, color='green')

# Выделение локального минимума с аннотацией
local_min_x = 2*np.pi / 3
local_min_y = f(local_min_x)
plt.scatter(local_min_x, local_min_y, color='red') # точка
plt.annotate('Локальный минимум', xy=(local_min_x, local_min_y), xytext=(-150, 30), textcoords='offset points',
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.5', color='red'))

# Добавление произвольного текста на график
plt.text(0, -1, 'Пример текста на графике', fontsize=12, color='purple')

# Добавление дополнительного графика для сравнения
x2 = np.linspace(-2*np.pi, 2*np.pi, 400)
y2 = np.sin(x2)
plt.plot(x2, y2, label='y = sin(x)', linestyle='--', color='gray')

# Добавление легенды
plt.legend()

# Отображение графика
plt.show()
