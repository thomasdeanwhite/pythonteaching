import matplotlib.pyplot as plt
import numpy as np
import sys
names = ['students', 'demonstrators', 'lecturers']
values = [[100, 100, 100], [50, 100, 100], [25, 100, 100], [12, 100, 100], [6, 100, 100]]

def basic_plot():
    # plot two lines
    plt.plot([1, 2, 3, 4])
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], "ro")

    plt.ylabel('some variable')
    plt.show()

def line_example():
    global names, values

    plots = []
    labels = []

    v = np.array(values)

    for i in range(len(names)):
        # [0] as plot gets wrapper in array
        plots.append(plt.plot(v[..., i])[0])

        labels.append(names[i])

    plt.legend(plots, labels)


    plt.ylabel('attendance percentage')
    plt.show()

def bar_example():
    global names, values
    plots = []
    labels = []
    plt.figure(1, figsize=(9, len(values)))
    for i in range(len(values)):
        # plot the bar chart and add to plots list
        plots.append(plt.bar(names, values[i]))

        # add label for this plot to labels list
        labels.append("Week {}".format(i))

    # set legend using plots and labels
    plt.legend(plots, labels)

    plt.ylabel('attendance percentage')
    plt.show()

method = line_example
method_name = "help"
if len(sys.argv) > 1:
    method_name = sys.argv[1]

print("Calling method {}.".format(method_name))

def help():
    print("Arguments: 'bar' or 'line' or 'basic'")

methods = {
    "bar":bar_example,
    "line":line_example,
    "basic":basic_plot,
    "help":help
}

if method_name in methods:
    method = methods[method_name]
else:
    method = help

method()