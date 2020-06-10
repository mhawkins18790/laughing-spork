import matplotlib.pyplot as pyplot

x_values = list(range(1, 5000))
y_values = [x**3 for x in x_values]

pyplot.cm = 'RdYlGn'

pyplot.scatter(x_values, y_values, c=y_values, cmap=pyplot.cm)

pyplot.show()
