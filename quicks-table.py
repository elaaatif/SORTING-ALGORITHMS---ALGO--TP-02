# pip install graphviz
from graphviz import Digraph
import os

def read_list_from_file(filename):
    with open(filename, 'r') as file:
        return [int(line.strip()) for line in file]

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        # Visualize the partitioning step
        visualize_quick_sort(arr, low, high, pi)

        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def visualize_quick_sort(arr, low, high, pivot):
    global quick_sort_steps
    quick_sort_steps.append((arr.copy(), low, high, pivot))

# Read the list from the file
file_name = 'num.txt'
original_list = read_list_from_file(file_name)

# Initialize step counter for QuickSort visualization
quick_sort_steps = []

# Visualize QuickSort steps
quicksort(original_list, 0, len(original_list) - 1)

# Generate HTML content
html_content = f'''
<!DOCTYPE html>
<link rel="stylesheet" type="text/css" href="styles.css">
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>QuickSort Visualization</title>
    <style>
        table {{
            border-collapse: collapse;
            width: 100%;
        }}
        th, td {{
            border: 1px solid black;
            padding: 8px;
            text-align: center;
        }}
        th {{
            background-color: #f2f2f2;
        }}
    </style>
</head>
<body>

<h1>QuickSort Visualization</h1>

<h2>Original List</h2>
<table>
    <tr>
        {" ".join(f'<th>{i}</th>' for i in range(len(original_list)))}
    </tr>
    <tr>
        {" ".join(f'<td>{value}</td>' for value in original_list)}
    </tr>
</table>

<h2>QuickSort Steps</h2>
'''

# Add QuickSort steps to HTML tables
for step, (step_list, low, high, pivot) in enumerate(quick_sort_steps, start=1):
    html_content += f'<h3>Step {step}</h3>\n'
    html_content += '<table>\n'
    html_content += '<tr>\n'
    for i, value in enumerate(step_list):
        if low <= i <= high:
            html_content += f'<td style="background-color: lightyellow;">{value}</td>'
        else:
            html_content += f'<td>{value}</td>'
    html_content += '</tr>\n'
    html_content += '</table>\n'

html_content += '''
</body>
</html>
'''
html_folder = 'html'
os.makedirs(html_folder, exist_ok=True)
html_file_path = os.path.join(html_folder, 'quicksort_visualization.html')
with open(html_file_path, 'w') as html_file:
    html_file.write(html_content)


# Open the HTML file in a web browser
import webbrowser
webbrowser.open('quicksort_visualization.html')
