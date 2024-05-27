import numpy as np
import matplotlib.pyplot as plt

# 定义 x 的范围 / Определение диапазона x
x = np.arange(0, 2 * np.pi, 0.2)

# 定义函数 / Определение функций
y1 = 0.5 * np.exp(-2 * x)
y2 = 60 * np.sin(3 * x)**5

# 第1部分：在一个窗口中绘制两个函数的图形 / Часть 1: Построение графиков двух функций в одном окне
plt.figure(figsize=(10, 6))

# 绘制 y1 / Построение y1
plt.plot(x, y1, color='brown', linestyle=':', marker='h', markersize=8, label='$y_1(x) = 0.5e^{-2x}$')

# 绘制 y2 / Построение y2
plt.plot(x, y2, color='blue', linestyle='-.', marker='o', markersize=8, label='$y_2(x) = 60\sin^5(3x)$')

# 添加标签和标题 / Добавление меток и заголовка
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('Графики $y_1(x)$ и $y_2(x)$')
plt.legend()
plt.grid(True)

# 显示图形 / Отображение графика
plt.show()

# 第2部分：使用至少500个点绘制一个函数的图形 / Часть 2: Построение графика одной функции с использованием не менее 500 точек
x_fine = np.linspace(0, 2 * np.pi, 500)
y1_fine = 0.5 * np.exp(-2 * x_fine)

plt.figure(figsize=(10, 6))
plt.plot(x_fine, y1_fine, color='brown', linestyle=':', marker='h', markersize=4, label='$y_1(x) = 0.5e^{-2x}$')

# 添加标签和标题 / Добавление меток и заголовка
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('График $y_1(x)$ с использованием 500 точек')
plt.legend()
plt.grid(True)

# 显示图形 / Отображение графика
plt.show()

# 第3部分：不同的标记方案 / Часть 3: Разные варианты маркировки
plt.figure(figsize=(15, 10))

plt.subplot(2, 2, 1)
plt.plot(x, y1, color='brown', linestyle='-', marker='h', markersize=8, label='$y_1(x)$')
plt.title('Параметры: color=brown, linestyle=-, marker=h')
plt.legend()
plt.grid(True)

plt.subplot(2, 2, 2)
plt.plot(x, y1, color='green', linestyle='--', marker='x', markersize=8, label='$y_1(x)$')
plt.title('Параметры: color=green, linestyle=--, marker=x')
plt.legend()
plt.grid(True)

plt.subplot(2, 2, 3)
plt.plot(x, y1, color='red', linestyle=':', marker='o', markersize=8, label='$y_1(x)$')
plt.title('Параметры: color=red, linestyle=:, marker=o')
plt.legend()
plt.grid(True)

plt.subplot(2, 2, 4)
plt.plot(x, y1, color='blue', linestyle='-.', marker='s', markersize=8, label='$y_1(x)$')
plt.title('Параметры: color=blue, linestyle=-., marker=s')
plt.legend()
plt.grid(True)

# 显示图形 / Отображение графиков
plt.tight_layout()
plt.show()

# 第4部分：带填充的图形 / Часть 4: Графики с заливкой
plt.figure(figsize=(10, 6))

plt.fill_between(x, y1, color="skyblue", alpha=0.4)
plt.plot(x, y1, color="Slateblue", alpha=0.6, linewidth=2, label='$y_1(x)$')

plt.fill_between(x, y2, color="lightcoral", alpha=0.4)
plt.plot(x, y2, color="darkred", alpha=0.6, linewidth=2, label='$y_2(x)$')

# 添加标签和标题 / Добавление меток и заголовка
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('Графики с заливкой $y_1(x)$ и $y_2(x)$')
plt.legend()
plt.grid(True)

# 显示图形 / Отображение графика
plt.show()

# 第5部分：裁剪图形 / Часть 5: Обрезка графиков
plt.figure(figsize=(10, 6))

plt.plot(x, y1, color='brown', linestyle=':', marker='h', markersize=8, label='$y_1(x) = 0.5e^{-2x}$')
plt.plot(x, y2, color='blue', linestyle='-.', marker='o', markersize=8, label='$y_2(x) = 60\sin^5(3x)$')

# 裁剪图形 / Обрезка графиков
plt.xlim(0, 4)
plt.ylim(0, 60)

# 添加标签和标题 / Добавление меток и заголовка
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('Обрезка графиков $y_1(x)$ и $y_2(x)$')
plt.legend()
plt.grid(True)

# 显示图形 / Отображение графика
plt.show()
