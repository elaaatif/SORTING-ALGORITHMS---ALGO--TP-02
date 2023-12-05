import random
import os
from graphviz import Digraph

# Function to perform quicksort
def quicksort(arr, depth=0):
    if not arr:
        return "", []

    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]

    tree_str = f'"{pivot}" [label="{pivot}", style="filled", fillcolor="#4680b8",fontcolor="white",fontname="Calibri"];\n'
    tree_str += quicksort(left, depth + 1)[0]
    tree_str += quicksort(right, depth + 1)[0]

    sorted_list = quicksort(left, depth + 1)[1] + [pivot] + quicksort(right, depth + 1)[1]

    return tree_str, sorted_list

# Function to draw the binary search tree
def draw_binary_tree_dot(root, dot, depth=0):
    if root is None:
        return

    dot.node(f'{root.value}', label=str(root.value), style="filled", fillcolor="#4680b8", fontcolor="white", fontname="Calibri")

    if root.left:
        dot.edge(f'{root.value}', f'{root.left.value}')
        draw_binary_tree_dot(root.left, dot, depth + 1)

    if root.right:
        dot.edge(f'{root.value}', f'{root.right.value}')
        draw_binary_tree_dot(root.right, dot, depth + 1)

# Node class for binary search tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Function to insert a node in the binary search tree
def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

# Function to visualize the binary search tree after each insertion
def visualize_tree_after_insertions(root, original_list, image_path_prefix):
    dot = Digraph(comment='Binary Search Tree')

    # Create a subfolder for visualization steps
    subfolder_path = os.path.join('.', 'vis-steps')
    os.makedirs(subfolder_path, exist_ok=True)

    for i, num in enumerate(original_list):
        root = insert(root, num)
        draw_binary_tree_dot(root, dot)

        # Render binary search tree DOT file to a PNG image in the subfolder
        image_path = os.path.join(subfolder_path, f'{image_path_prefix}_step_{i+1}')
        dot.render(image_path, format='png', cleanup=True)

    # Render the final binary search tree DOT file to a PNG image in the subfolder
    final_image_path = os.path.join(subfolder_path, f'{image_path_prefix}_final')
    draw_binary_tree_dot(root, dot)
    dot.render(final_image_path, format='png', cleanup=True)

# Read the list from a text file
def read_list_from_file(filename):
    with open(filename, 'r') as file:
        return [int(line.strip()) for line in file]

# Specify the file name containing the list of numbers
file_name = 'num.txt'  # Change this to the actual file name

# Read the list from the file
original_list = read_list_from_file(file_name)

# Create binary search tree
binary_search_tree = None

# Check if the number of elements is less than or equal to 10
if len(original_list) <= 10:
    visualize_tree_after_insertions(binary_search_tree, original_list, 'binary_tree_insertions')

# Generate DOT source for quicksort tree and get the sorted list
quicksort_dot, quicksort_sorted_list = quicksort(original_list)

# Save DOT source to files
with open('quicksort_tree.dot', 'w') as quicksort_file:
    quicksort_file.write(quicksort_dot)

# Render quicksort DOT file to a PNG image
quicksort_image_path = 'quicksort_tree'
dot_quicksort = Digraph(comment='Quicksort Tree')
dot_quicksort.render(quicksort_image_path, format='png', cleanup=True)

# Generate HTML content
html_content = f'''
<!DOCTYPE html>
<html lang="en">
<link rel="stylesheet" type="text/css" href="styles.css">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tree Visualization</title>
</head>
<body>

<h1>Tree Visualization</h1>

<h2>Original List</h2>
<table border="1">
    <tr>
        <!-- Header Row -->
        {" ".join(f'<th>{i}</th>' for i in range(len(original_list)))}
    </tr>
    <tr>
        <!-- Values Row -->
        {" ".join(f'<td>{value}</td>' for value in original_list)}
    </tr>
</table>

<h2>Quicksort Tree Visualization</h2>
<img src="{quicksort_image_path}.png" alt="Quicksort Tree" style="max-width: 100%;">

<h2>Sorted List (Quicksort)</h2>
<table border="1">
    <tr>
        <!-- Header Row -->
        {" ".join(f'<th>{i}</th>' for i in range(len(quicksort_sorted_list)))}
    </tr>
    <tr>
        <!-- Values Row -->
        {" ".join(f'<td>{value}</td>' for value in quicksort_sorted_list)}
    </tr>
</table>

<!-- Include the images for binary search tree insertions -->
{"".join(f'<h2>Binary Search Tree After Insertion {i+1}</h2><img src="vis-steps/{f"binary_tree_insertions_step_{i+1}.png"}" alt="Binary Search Tree" style="max-width: 100%;">' for i in range(len(original_list)))}

<h2>Final Binary Search Tree Visualization</h2>
<img src="{f'binary_tree_insertions_final.png'}" alt="Final Binary Search Tree" style="max-width: 100%;">

</body>
</html>
'''

# Save HTML content to a file
with open('tree_visualization.html', 'w') as html_file:
    html_file.write(html_content)

# Open the HTML file in a web browser
import webbrowser
webbrowser.open('tree_visualization.html')
