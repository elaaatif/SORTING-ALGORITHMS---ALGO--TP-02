#(https://graphviz.gitlab.io/download/) to visualize the DOT files as images. need to download it /add path to sys vars & import it later.
#pip install graphviz
#pip install graphviz
from graphviz import Digraph
import os

# Read the list from a text file
def read_list_from_file(filename):
    with open(filename, 'r') as file:
        return [int(line.strip()) for line in file]

# Node class for the tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Function to perform quicksort and generate a tree
def quicksort_tree(arr, depth=0, parent=None):
    if not arr:
        return None, "", []

    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]

    root = Node(pivot)
    
    left_tree, left_str, left_sorted = quicksort_tree(left, depth + 1, pivot)
    right_tree, right_str, right_sorted = quicksort_tree(right, depth + 1, pivot)

    root.left = left_tree
    root.right = right_tree

    tree_str = f'"{pivot}" [label="{pivot}", fillcolor="#4680b8", style="filled"];\n'
    tree_str += left_str + right_str

    sorted_list = left_sorted + [pivot] + right_sorted

    return root, tree_str, sorted_list

# Read the list from the file
file_name = 'numbers.txt'  # Change this to the actual file name
original_list = read_list_from_file(file_name)

# Update to use quicksort_tree instead of quicksort
quicksort_root, quicksort_dot, quicksort_sorted_list = quicksort_tree(original_list)

# Print the DOT representation for debugging
print(quicksort_dot)

# Create directories if they don't exist
gen_dot_folder = 'gen-dot-file'
gen_png_folder = 'gen-png'

os.makedirs(gen_dot_folder, exist_ok=True)
os.makedirs(gen_png_folder, exist_ok=True)

# Save DOT source to files
quicksort_dot_file_path = os.path.join(gen_dot_folder, 'quicksort_tree.dot')
with open(quicksort_dot_file_path, 'w') as quicksort_file:
    quicksort_file.write(f'digraph G {{\n{quicksort_dot}}}')

# Print the DOT file path for debugging
print(f"Quicksort DOT file saved at: {quicksort_dot_file_path}")

# Render quicksort DOT file to a PNG image
quicksort_image_path = os.path.join(gen_png_folder, 'quicksort_tree')
dot_quicksort = Digraph(comment='Quicksort Tree')
dot_quicksort.render(quicksort_image_path, format='png', cleanup=True)

# Print the image path for debugging
print(f"Quicksort PNG image saved at: {quicksort_image_path}.png")
# ...


#----------------------------------------------------------------
#----------------------------------------------------------------
#----------------------------------------------------------------



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





# Create binary search tree
binary_search_tree = None
for num in original_list:
    binary_search_tree = insert(binary_search_tree, num)


binary_search_tree_dot = Digraph(comment='Binary Search Tree')
draw_binary_tree_dot(binary_search_tree, binary_search_tree_dot)
with open('binary_tree.dot', 'w') as binary_tree_file:
    binary_tree_file.write(binary_search_tree_dot.source)

binary_search_tree_dot_file_path = os.path.join(gen_dot_folder, 'binary_tree.dot')
with open(binary_search_tree_dot_file_path, 'w') as binary_tree_file:
    binary_tree_file.write(binary_search_tree_dot.source)

# Render binary search tree DOT file to a PNG image
binary_search_tree_image_path = os.path.join(gen_png_folder, 'binary_tree')
binary_search_tree_dot.render(binary_search_tree_image_path, format='png', cleanup=True)

# Generate HTML content
html_content = f'''
<!DOCTYPE html>
<link rel="stylesheet" type="text/css" href="styles.css">
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

<h2>Binary Search Tree Visualization</h2>
<img src="{binary_search_tree_image_path}.png" alt="Binary Search Tree" style="max-width: 100%;">

</body>
</html>
'''
html_folder = 'html'
os.makedirs(html_folder, exist_ok=True)
html_file_path = os.path.join(html_folder, 'tree_visualization.html')
with open(html_file_path, 'w') as html_file:
    html_file.write(html_content)


# Open the HTML file in a web browser
import webbrowser
webbrowser.open('tree_visualization.html')
