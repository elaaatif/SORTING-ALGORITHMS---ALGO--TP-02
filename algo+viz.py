#pip install graphviz
import random
from graphviz import Digraph

# Function to perform quicksort
def quicksort(arr, depth=0):
    if not arr:
        return ""

    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]

    tree_str = f'"{pivot}" [label="{pivot}"];\n'
    tree_str += quicksort(left, depth + 1)
    tree_str += quicksort(right, depth + 1)
    return tree_str

# Function to draw the binary search tree
def draw_binary_tree_dot(root, dot, depth=0):
    if root is None:
        return ""

    tree_str = f'"{root.value}" [label="{root.value}"];\n'
    if root.left:
        tree_str += f'"{root.value}" -> "{root.left.value}";\n'
    if root.right:
        tree_str += f'"{root.value}" -> "{root.right.value}";\n'

    tree_str += draw_binary_tree_dot(root.left, dot, depth + 1)
    tree_str += draw_binary_tree_dot(root.right, dot, depth + 1)

    dot.node(f'{root.value}', label=str(root.value))

    if root.left:
        dot.edge(f'{root.value}', f'{root.left.value}')
    if root.right:
        dot.edge(f'{root.value}', f'{root.right.value}')

    return tree_str

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

# Read the list from a text file
def read_list_from_file(filename):
    with open(filename, 'r') as file:
        return [int(line.strip()) for line in file]

# Specify the file name containing the list of numbers
file_name = 'numbers.txt'  # Change this to the actual file name

# Read the list from the file
original_list = read_list_from_file(file_name)

# Create binary search tree
bst = None
for num in original_list:
    bst = insert(bst, num)

# Generate DOT source for quicksort tree
quicksort_dot = 'digraph G {' + quicksort(original_list) + '}'

# Generate DOT source for binary search tree
dot = Digraph(comment='Binary Search Tree')
draw_binary_tree_dot(bst, dot)

# Save DOT source to files
with open('quicksort_tree.dot', 'w') as quicksort_file:
    quicksort_file.write(quicksort_dot)

dot.render('binary_tree', format='png', cleanup=True)

# Generate HTML content
html_content = f'''
<!DOCTYPE html>
<html lang="en">
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
        <th>Index</th>
        <th>Value</th>
    </tr>
'''
# Populate the table
for i, value in enumerate(original_list):
    html_content += f'<tr><td>{i}</td><td>{value}</td></tr>'

# Add quicksort tree visualization
html_content += f'''
</table>

<h2>Quicksort Tree Visualization</h2>
<img src="quicksort_tree.png" alt="Quicksort Tree" style="max-width: 100%;">

<h2>Binary Search Tree Visualization</h2>
<img src="binary_tree.png" alt="Binary Search Tree" style="max-width: 100%;">

</body>
</html>
'''

# Save HTML content to a file
with open('tree_visualization.html', 'w') as html_file:
    html_file.write(html_content)

# Open the HTML file in a web browser
import webbrowser
webbrowser.open('tree_visualization.html')
