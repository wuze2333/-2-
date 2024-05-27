import numpy as np
import matplotlib.pyplot as plt

# 定义函数
def y(x):
    return 6 * np.cos(5 * x)

# 定义区间和步长
x_values = np.arange(0, 2 * np.pi + 0.2, 0.2)
y_values = y(x_values)

# 创建 stem 图
plt.figure(figsize=(10, 6))
markerline, stemlines, baseline = plt.stem(x_values, y_values, linefmt='r--', markerfmt='rd', basefmt='k-')

# 设置参数
plt.setp(markerline, 'markersize', 8)
plt.setp(stemlines, 'linewidth', 1.5)
plt.setp(baseline, 'linewidth', 1)

# 定制图形
plt.title(r'Stem plot of $y(x) = 6 \cos(5x)$')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.grid(True)

# 显示图形
plt.show()
