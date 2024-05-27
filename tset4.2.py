import matplotlib.pyplot as plt
import numpy as np

# 年份数据 / Данные по годам
years = np.array([2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023])

# 变量数据 / Данные переменных
X3_L = np.array([222.0, 32.0, 82.0, 45.2, 299.3, 41.6, 17.8, 151.0, 82.3, 103.0, 225.4, 675.0, 43.8, 102.3, 105.0, 49.1, 50.4, 480.0, 71.0, 43.0])
X3_price = np.array([13.0, 16.5, 17.0, 15.0, 14.2, 10.5, 23.0, 12.0, 22.5, 26.0, 18.5, 13.2, 25.8, 17.0, 18.0, 21.0, 15.5, 38.0, 30.0, 24.0])
X3_kitchen_area = np.array([6.5, 22.4, 15.0, 13.0, 9.0, 5.6, 8.5, 5.5, 8.0, 8.0, 6.0, 13.0, 10.0, 8.7, 10.0, 7.2, 24.0, 20.0, 7.5])
X3_inflation = np.array([10.3, 11.4, 12.2, 11.5, 11.2, 10.5, 9.4, 9.5, 9.3, 9.2, 9.4, 9.7, 8.2, 8.4, 8.2, 8.1, 7.8, 7.2, 8.2, 7.5])
X3_labour_costs = np.array([20.18, 18.59, 15.78, 9.00, 23.05, 14.37, 19.61, 17.16, 5.07, 0.43, 98.04, 52.10, 13.68, 4.16, 17.40, 10.43, 66.70, 12.27, 11.67, 81.50])

# 散点图 - 年份与 X3_劳动成本 之间的关系 / Точечный график - взаимосвязь между годами и затратами на труд
plt.figure(figsize=(10, 6))
plt.scatter(years, X3_labour_costs, color='blue', marker='o')
plt.title('Scatter Plot of Labour Costs Over Years')  # 添加标题 / Добавление заголовка
plt.xlabel('Year')  # 设置 x 轴标签 / Установка метки оси x
plt.ylabel('Labour Costs')  # 设置 y 轴标签 / Установка метки оси y
plt.grid(True)  # 添加网格 / Добавление сетки
plt.show()

# 柱状图 - 年份与 X3_劳动成本 之间的关系 / Гистограмма - взаимосвязь между годами и затратами на труд
plt.figure(figsize=(10, 6))
plt.bar(years, X3_labour_costs, color='orange')
plt.title('Bar Chart of Labour Costs Over Years')  # 添加标题 / Добавление заголовка
plt.xlabel('Year')  # 设置 x 轴标签 / Установка метки оси x
plt.ylabel('Labour Costs')  # 设置 y 轴标签 / Установка метки оси y
plt.grid(True)  # 添加网格 / Добавление сетки
plt.show()

# 饼图 - 显示 2023 年劳动成本的组成部分/ Круговая диаграмма - состав затрат на труд в 2023 году
parts = [20, 30, 25, 25]
labels = ['Part A', 'Part B', 'Part C', 'Part D']
plt.figure(figsize=(8, 8))
plt.pie(parts, labels=labels, autopct='%1.1f%%', colors=['gold', 'yellowgreen', 'lightcoral', 'lightskyblue'])
plt.title('Pie Chart of Labour Costs Composition in 2023')  # 添加标题 / Добавление заголовка
plt.show()
