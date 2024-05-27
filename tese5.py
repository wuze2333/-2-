import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 加载企鹅数据集
penguins = sns.load_dataset("penguins")

# 数据集描述
print("Информация о наборе данных:")  # 数据集信息
print(penguins.info())
print("\nСтатистическое описание набора данных:")  # 数据集统计描述
print(penguins.describe())

# 检查缺失数据
print("\nОтсутствующие данные:")  # 缺失数据情况
print(penguins.isnull().sum())

# 删除缺失数据
penguins_cleaned = penguins.dropna()

# 验证缺失数据处理结果
print("\nПосле обработки отсутствующих данных:")  # 缺失数据处理后
print(penguins_cleaned.isnull().sum())

# 企鹅种类数量
plt.figure(figsize=(10, 6))
sns.countplot(data=penguins_cleaned, x='species')
plt.title('Количество видов пингвинов')  # 企鹅种类数量
plt.xlabel('Вид')  # 种类
plt.ylabel('Количество')  # 数量
plt.show()
print("Вывод: Диаграмма количества видов пингвинов показывает, что пингвинов вида Adelie больше всего, а пингвинов вида Chinstrap меньше всего.")  # 分析结论：企鹅种类数量图表显示，Adelie企鹅数量最多，Chinstrap企鹅数量最少。

# 不同岛屿上的企鹅数量
plt.figure(figsize=(10, 6))
sns.countplot(data=penguins_cleaned, x='island', hue='species')
plt.title('Количество видов пингвинов на разных островах')  # 不同岛屿上的企鹅种类数量
plt.xlabel('Остров')  # 岛屿
plt.ylabel('Количество')  # 数量
plt.legend(title='Вид')  # 种类
plt.show()
print("Вывод: Диаграмма количества видов пингвинов на разных островах показывает, что пингвины вида Adelie распространены на всех островах, тогда как пингвины видов Chinstrap и Gentoo сконцентрированы на определенных островах.")  # 分析结论：不同岛屿上的企鹅种类数量图表显示，Adelie企鹅分布在所有岛屿，而Chinstrap和Gentoo企鹅分别集中在特定岛屿。

# 鳍长分布
plt.figure(figsize=(10, 6))
sns.histplot(data=penguins_cleaned, x='flipper_length_mm', hue='species', kde=True)
plt.title('Распределение длины плавника у пингвинов')  # 企鹅的鳍长分布
plt.xlabel('Длина плавника (мм)')  # 鳍长 (mm)
plt.ylabel('Количество')  # 数量
plt.legend(title='Вид')  # 种类
plt.show()
print("Вывод: Диаграмма распределения длины плавника показывает, что длина плавников у пингвинов вида Gentoo заметно больше, чем у других видов.")  # 分析结论：鳍长分布图表显示，Gentoo企鹅的鳍长度明显长于其他种类。

# 喙长度与深度的关系
plt.figure(figsize=(10, 6))
sns.scatterplot(data=penguins_cleaned, x='bill_length_mm', y='bill_depth_mm', hue='species')
plt.title('Взаимосвязь длины и глубины клюва у пингвинов')  # 企鹅喙长度与深度的关系
plt.xlabel('Длина клюва (мм)')  # 喙长 (mm)
plt.ylabel('Глубина клюва (мм)')  # 喙深 (mm)
plt.legend(title='Вид')  # 种类
plt.show()
print("Вывод: Диаграмма взаимосвязи длины и глубины клюва показывает, что у разных видов пингвинов размеры клюва различаются.")  # 分析结论：喙长度与深度的关系图表显示，不同种类企鹅的喙尺寸特征有明显差异。

# 体重与鳍长的线性回归
plt.figure(figsize=(10, 6))
sns.lmplot(data=penguins_cleaned, x='body_mass_g', y='flipper_length_mm', hue='species')
plt.title('Линейная регрессия массы тела и длины плавника у пингвинов')  # 企鹅体重与鳍长的线性回归
plt.xlabel('Масса тела (г)')  # 体重 (g)
plt.ylabel('Длина плавника (мм)')  # 鳍长 (mm)
plt.legend(title='Вид')  # 种类
plt.show()
print("Вывод: Диаграмма линейной регрессии массы тела и длины плавника показывает, что между массой тела и длиной плавника у пингвинов существует положительная корреляция.")  # 分析结论：体重与鳍长的线性回归图表显示，企鹅的体重与鳍长度之间存在正相关关系。

# 箱线图
plt.figure(figsize=(10, 6))
sns.boxplot(data=penguins_cleaned, x='species', y='flipper_length_mm')
plt.title('Распределение длины плавника у разных видов пингвинов')  # 不同种类企鹅的鳍长分布
plt.xlabel('Вид')  # 种类
plt.ylabel('Длина плавника (мм)')  # 鳍长 (mm)
plt.show()
print("Вывод: Диаграмма распределения длины плавника показывает, что длина плавников у разных видов пингвинов существенно различается, и у пингвинов вида Gentoo она больше.")  # 分析结论：箱线图显示，不同种类企鹅的鳍长分布存在显著差异，Gentoo企鹅的鳍长分布较高。

# 联合图
plt.figure(figsize=(10, 6))
sns.jointplot(data=penguins_cleaned, x='bill_length_mm', y='bill_depth_mm', hue='species', kind='scatter')
plt.suptitle('Взаимосвязь длины и глубины клюва у пингвинов', y=1.02)  # 企鹅喙长度与深度的关系
plt.xlabel('Длина клюва (мм)')
plt.ylabel('Глубина клюва (мм)')
plt.show()
print("Вывод: Совмещенная диаграмма показывает, что взаимосвязь длины и глубины клюва у разных видов пингвинов заметно различается.")  # 分析结论：联合图显示，不同种类企鹅的喙长度与深度的关系存在明显差异。

# 相关性热图
plt.figure(figsize=(12, 8))
correlation_matrix = penguins_cleaned.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Корреляция между характеристиками пингвинов')  # 企鹅特征之间的相关性
plt.show()
print("Вывод: Тепловая карта корреляции показывает, что между массой тела и длиной плавника у пингвинов существует сильная положительная корреляция.")  # 分析结论：相关性热图显示，企鹅体重与鳍长之间存在较强的正相关关系。

# 不同种类企鹅的体重分布（新增图表）
plt.figure(figsize=(10, 6))
sns.boxplot(data=penguins_cleaned, x='species', y='body_mass_g')
plt.title('Распределение массы тела у разных видов пингвинов')  # 不同种类企鹅的体重分布
plt.xlabel('Вид')  # 种类
plt.ylabel('Масса тела (г)')  # 体重 (g)
plt.show()
print("Вывод: Диаграмма распределения массы тела показывает, что масса тела у пингвинов вида Gentoo существенно больше, чем у других видов.")  # 分析结论：不同种类企鹅的体重大大高于其他种类。

# 综合总结
print("Общий вывод:")  # 综合总结
print("Анализ набора данных о пингвинах показал, что пингвинов вида Adelie больше всего, и они наиболее широко распространены.")  # 通过对企鹅数据集的分析，我们发现Adelie企鹅的数量最多，分布最广。
print("Пингвины вида Gentoo имеют заметно большую длину плавников и массу тела по сравнению с другими видами.")  # Gentoo企鹅的鳍长和体重显著大于其他种类。
print("У разных видов пингвинов длина и глубина клюва существенно различаются.")  # 不同种类企鹅的喙长度与深度存在明显差异。
print("Между массой тела и длиной плавника у пингвинов существует положительная корреляция.")  # 企鹅体重与鳍长之间存在正相关关系。
print("В целом, различные виды пингвинов имеют заметные различия в различных характеристиках, которые можно наглядно показать с помощью различных методов визуализации.")  # 总体来说，不同种类企鹅在各个特征上的表现存在显著差异，这些差异可以通过多种可视化方法清晰地展示出来。
