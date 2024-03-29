import time
import csv
import matplotlib.pyplot as plt
import mplcursors
import matplotlib.animation as anim

if __name__ == '__main__':
    # Read in a csv - sort by type
    csv_name = 'test.csv'
    transcript_name = 'transcripts/text1568559661.txt'

    graph_data = {}
    # Table format: time, type, value
    with open(csv_name) as csv_file:
        with open(transcript_name, 'r') as transcript:
            transcript_times = []
            transcript_values = []

            for line in transcript.readlines():
                line = line.split('    ')
                line[1] = line[1].split(':')
                line[1] = int(line[1][0]) * 60 + int(line[1][1])
                line[2] = f'{line[0]}: {line[2]}'
                transcript_times += [line[1]]
                transcript_values += [line[2]]

            print(transcript_times)
            print(transcript_values)

            fig, ax = plt.subplots()

            lines = {}

            for i in range(len(transcript_times)):
                line = plt.plot([transcript_times[i]] * 2, [0, 1], label=transcript_values[i])
                lines[transcript_times[i]] = transcript_values[i]

            mplcursors.cursor(ax).connect(
                "add", lambda sel: sel.annotation.set_text(sel.artist.get_label())
            )

            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                # Check if the type already exists in the dictionary
                if row[1] not in graph_data.keys():
                    graph_data[row[1]] = {'time': [], 'value': []}
                # Add the point to the right slot in the dictionary
                graph_data[row[1]]['time'].append(float(row[0]))
                graph_data[row[1]]['value'].append(float(row[2]))

            min_time = min([min(graph_data[entry]['time']) for entry in graph_data])

    # Plot time on the x axis - all the other data points on the same graph
    keys = []
    for key in graph_data:
        keys += plt.plot([time - min_time for time in graph_data[key]['time']], graph_data[key]['value'], label=key)
    print(keys)
    plt.legend(handles=keys)
    plt.xlabel('time (s)')

    plt.show()
