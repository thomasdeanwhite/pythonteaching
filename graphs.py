import matplotlib.pyplot as plt
import numpy as np

names = ['students', 'demonstrators', 'lecturers']
values = [[100, 100, 100], [50, 100, 100], [25, 100, 100], [12, 100, 100], [6, 100, 100]]

def basic_plot():
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

line_example()