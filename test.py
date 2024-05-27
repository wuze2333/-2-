import matplotlib.pyplot as plt
import numpy as np

# Define the function given in the image
def f(x):
    return np.cos(x) + (np.sqrt(3)/2)*x - 1/2

# Generate x values
x = np.linspace(-2*np.pi, 2*np.pi, 400)

# Compute y values
y = f(x)

# Plot the function
plt.figure(figsize=(10, 5))
plt.plot(x, y, label='y = cos(x) + (sqrt(3)/2)*x - 1/2')

# Adding title and labels with custom fonts
plt.title('Function Plot: $y = \cos(x) + \\frac{\sqrt{3}}{2}x - \\frac{1}{2}$', fontsize=14, fontweight='bold')
plt.xlabel('X-axis', fontsize=12, color='blue')
plt.ylabel('Y-axis', fontsize=12, color='green')

# Highlighting a local minimum with annotation
local_min_x = 2*np.pi / 3
local_min_y = f(local_min_x)
plt.scatter(local_min_x, local_min_y, color='red') # point
plt.annotate('Local Minimum', xy=(local_min_x, local_min_y), xytext=(-150, 30), textcoords='offset points',
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.5', color='red'))

# Adding arbitrary text to the graph
plt.text(0, -1, 'Sample text on the graph', fontsize=12, color='purple')

# Add an additional plot for comparison
x2 = np.linspace(-2*np.pi, 2*np.pi, 400)
y2 = np.sin(x2)
plt.plot(x2, y2, label='y = sin(x)', linestyle='--', color='gray')

# Adding a legend
plt.legend()

# Show the plot
plt.show()