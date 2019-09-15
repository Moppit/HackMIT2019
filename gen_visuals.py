import time
import csv
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import numpy as np
import pandas as pd

if __name__ == '__main__':
    # Read in a csv - sort by type
    csv_name = 'test.csv'
    graph_data = {}
    # Table format: time, type, value
    with open(csv_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            # Check if the type already exists in the dictionary
            if row[1] not in graph_data.keys():
                graph_data[row[1]] = {'time':[], 'value':[]}
            # Add the point to the right slot in the dictionary
            graph_data[row[1]]['time'].append(float(row[0]))
            graph_data[row[1]]['value'].append(float(row[2]))

    # Plot time on the x axis - all the other data points on the same graph
    for key in graph_data:
        plt.plot(graph_data[key]['time'], graph_data[key]['value'], label=key)
    plt.legend()
    plt.show()
