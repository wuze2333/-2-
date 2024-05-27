import numpy as np
import matplotlib.pyplot as plt

# Define the range for x
x = np.arange(0, 2 * np.pi, 0.2)

# Define the functions
y1 = 0.5 * np.exp(-2 * x)
y2 = 6 * np.sin(3 * x)**2

# Plot the functions
plt.figure(figsize=(10, 6))

# Plot y1 with specified parameters
plt.plot(x, y1, 'brown', linestyle=':', marker='h', markersize=8, label='$y_1(x) = 0.5e^{-2x}$')

# Plot y2 with specified parameters
plt.plot(x, y2, 'blue', linestyle='-.', marker='o', markersize=8, label='$y_2(x) = 6\sin^2(3x)$')

# Add labels and title
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('Plots of $y_1(x)$ and $y_2(x)$')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
