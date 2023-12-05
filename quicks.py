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
    global quick_sort_step
    quick_sort_step += 1

    # Create a new graph for each step
    dot = Digraph(comment=f'QuickSort Step {quick_sort_step}')
    dot.node_attr.update(style='filled', color='lightblue')

    for i, value in enumerate(arr):
        if i == pivot:
            dot.node(f'{i}', label=str(value), color='lightcoral')
        elif low <= i <= high:
            dot.node(f'{i}', label=str(value), color='lightyellow')
        else:
            dot.node(f'{i}', label=str(value))

    # Save the DOT file
    dot_file_path = os.path.join(gen_dot_folder, f'quick_sort_step_{quick_sort_step}.dot')
    dot.render(dot_file_path, format='png', cleanup=True)

# Read the list from the file
file_name = 'numbers.txt'
original_list = read_list_from_file(file_name)

# Create directories if they don't exist
gen_dot_folder = 'gen-dot-file'
gen_png_folder = 'gen-png'
os.makedirs(gen_dot_folder, exist_ok=True)
os.makedirs(gen_png_folder, exist_ok=True)

# Initialize step counter for QuickSort visualization
quick_sort_step = 0

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
</head>
<body>

<h1>QuickSort Visualization</h1>

<h2>Original List</h2>
<table border="1">
    <tr>
        {" ".join(f'<th>{i}</th>' for i in range(len(original_list)))}
    </tr>
    <tr>
        {" ".join(f'<td>{value}</td>' for value in original_list)}
    </tr>
</table>

<h2>QuickSort Steps</h2>
'''
# Add QuickSort step images to HTML
for step in range(1, quick_sort_step + 1):
    html_content += f'<h3>Step {step}</h3>\n'
    html_content += f'<img src="{gen_png_folder}/quick_sort_step_{step}.png" alt="QuickSort Step {step}" style="max-width: 100%;">\n'

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
