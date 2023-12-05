'''example figure of triangle target + sqaure flankers'''

import matplotlib.pyplot as plt

# Set explicit axis limits
plt.xlim(35,65)
plt.ylim(49,51)
plt.xticks([])
plt.yticks([]) 


# Plotting symbols for a triangle of squares
plt.plot(50, 50, marker='^', color='k', markersize=28, markerfacecolor='k')

# Square 1
plt.plot(47.5, 50, marker='s', color='k', markersize=28, markerfacecolor='k', linewidth=0)

# Square 2
plt.plot(45, 50, marker='s', color='k', markersize=28, markerfacecolor='k', linewidth=0)

# Square 3
plt.plot(42.5, 50, marker='s', color='k', markersize=28, markerfacecolor='k', linewidth=0)

# Square 5
plt.plot(52.5, 50, marker='s', color='k', markersize=28, markerfacecolor='k', linewidth=0)

# Square 6
plt.plot(55, 50, marker='s', color='k', markersize=28, markerfacecolor='k', linewidth=0)

# Square 7
plt.plot(57.5, 50, marker='s', color='k', markersize=28, markerfacecolor='k', linewidth=0)

# Show the plot
plt.show()
