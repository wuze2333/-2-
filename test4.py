import numpy as np
import matplotlib.pyplot as plt

# 定义函数
def y(x):
    return np.arccos(2 * x)

# 定义区间和步长
x_values = np.arange(0, 0.5 + 0.06, 0.06)
y_values = y(x_values)

# 创建阶梯图
plt.figure(figsize=(10, 6))
plt.step(x_values, y_values, where='mid', color='maroon', linestyle='-', marker='<', markersize=8, markerfacecolor='maroon', markeredgewidth=2)

# 定制图形
plt.title(r'Stair-step plot of $y(x) = \arccos(2x)$')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.grid(True)

# 显示图形
plt.show()
