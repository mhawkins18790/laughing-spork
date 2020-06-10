import matplotlib.pyplot as pyplot

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

pyplot.cm = 'Blues'


pyplot.scatter(x_values, y_values, c=y_values,
               cmap=pyplot.cm, edgecolors='none', s=40)
pyplot.axis([0, 1100, 0, 1100000])

# Set chart title and label axes.
pyplot.title("Square Numbers", fontsize=24)
pyplot.xlabel("Value", fontsize=14)
pyplot.ylabel("Square of Value", fontsize=14)

# Set size of tick labels
pyplot.tick_params(axis='both', labelsize=14)


# pyplot.show()
pyplot.savefig('squares_plot.png', bbox_inches='tight')
