from graphviz import Digraph
import os
import time
import webbrowser

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def read_list_from_file(filename):
    with open(filename, 'r') as file:
        return [int(line.strip()) for line in file]

def draw_linked_list_dot(head, dot):
    current = head
    while current:
        dot.node(str(current.value), label=str(current.value))
        if current.next:
            dot.edge(str(current.value), str(current.next.value))
        current = current.next

def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.value))
        if root.next is not None:
            print_tree(root.next, level + 1, "L-- ")

def radix_sort_linked_list(input_list, gen_dot_folder, gen_png_folder):
    head = Node(input_list[0])
    current = head
    for value in input_list[1:]:
        current.next = Node(value)
        current = current.next

    radix_sort_dot = Digraph(comment='Radix Sort Linked List')

    max_digits = max(map(lambda x: len(str(x)), input_list))

    for place in range(1, 10 ** max_digits):
        buckets = [None] * 10
        current = head
        new_head = None
        new_tail = None

        while current:
            next_node = current.next
            current.next = None

            digit = (current.value // place) % 10
            if buckets[digit] is None:
                buckets[digit] = current
                new_head = current
                new_tail = current
            else:
                new_tail.next = current
                new_tail = current

            current = next_node

        head = new_head
        tail = new_tail

        for i in range(10):
            if buckets[i] is not None:
                tail.next = buckets[i]
                tail = buckets[i]

        draw_linked_list_dot(head, radix_sort_dot)
        radix_sort_dot_file_path = os.path.join(gen_dot_folder, f'radix_sort_linked_list_{place}.dot')

        with open(radix_sort_dot_file_path, 'w') as radix_sort_file:
            radix_sort_file.write(radix_sort_dot.source)

    # Save the final DOT file
    final_dot_file_path = os.path.join(gen_dot_folder, 'radix_sort_linked_list_final.dot')
    with open(final_dot_file_path, 'w') as final_dot_file:
        final_dot_file.write(radix_sort_dot.source)

    # Render and save the final PNG file
    try:
        radix_sort_dot.render(os.path.join(gen_png_folder, 'radix_sort_linked_list'), format='png', cleanup=True)
    except Exception as e:
        print(f"Error during rendering: {e}")

    return head, os.path.join(gen_png_folder, 'radix_sort_linked_list.png')

# Read the list from the file
file_name = 'num.txt'  # Change this to the actual file name
original_list = read_list_from_file(file_name)

# Create directories if they don't exist
gen_dot_folder = 'gen-dot-file'
gen_png_folder = 'gen-png'
os.makedirs(gen_dot_folder, exist_ok=True)
os.makedirs(gen_png_folder, exist_ok=True)

# Perform Radix Sort on the linked list
try:
    sorted_linked_list_head, radix_sort_image_path = radix_sort_linked_list(original_list, gen_dot_folder, gen_png_folder)
except Exception as e:
    print(f"Error during Radix Sort: {e}")

# Introduce a longer delay to allow time for Graphviz to complete rendering
time.sleep(5)

# Print the sorted tree in the terminal
print("Sorted Tree:")
print_tree(sorted_linked_list_head)

# Generate HTML content
html_content = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Radix Sort Visualization</title>
</head>
<body>

<h1>Radix Sort Visualization</h1>

<h2>Original List</h2>
<table border="1">
    <tr>
        {" ".join(f'<th>{i}</th>' for i in range(len(original_list)))}
    </tr>
    <tr>
        {" ".join(f'<td>{value}</td>' for value in original_list)}
    </tr>
</table>

<h2>Radix Sort Linked List Visualization</h2>
<img src="{radix_sort_image_path}" alt="Radix Sort Linked List" style="max-width: 100%;">

</body>
</html>
'''
html_folder = 'html'
os.makedirs(html_folder, exist_ok=True)
html_file_path = os.path.join(html_folder, 'radix_sort_visualization.html')
with open(html_file_path, 'w') as html_file:
    html_file.write(html_content)


# Open the HTML file in a web browser
webbrowser.open('radix_sort_visualization.html')
