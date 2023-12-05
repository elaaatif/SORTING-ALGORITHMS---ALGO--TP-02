import random

# Function to perform selection sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Function to perform merge sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Function to perform quicksort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        # Choose the minimum element as the pivot
        pivot = min(arr)
        
        # Partition the array into elements less than and greater than the pivot
        left = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        
        # Recursively apply quicksort to the sub-arrays
        return quicksort(left) + equal + quicksort(right)

# Function to draw the quicksort tree
def draw_quicksort_tree(arr, depth=0):
    if not arr:
        return ""

    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]

    tree_str = "  " * depth + str(pivot) + "\n"
    tree_str += draw_quicksort_tree(left, depth + 1)
    tree_str += draw_quicksort_tree(right, depth + 1)

    return tree_str

# Node class for binary search tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Function to insert a node in binary search tree
def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

# Function to draw the binary search tree
def draw_binary_tree(root, depth=0):
    if root is None:
        return ""

    tree_str = "  " * depth + str(root.value) + "\n"
    tree_str += draw_binary_tree(root.left, depth + 1)
    tree_str += draw_binary_tree(root.right, depth + 1)

    return tree_str

# Function to perform inorder traversal of binary search tree
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)

# Read the list from a text file
def read_list_from_file(filename):
    with open(filename, 'r') as file:
        return [int(line.strip()) for line in file]

# Specify the file name containing the list of numbers
file_name = 'numbers.txt'  # Change this to the actual file name

# Read the list from the file
original_list = read_list_from_file(file_name)

# Apply sorting algorithms
sorted_selection = selection_sort(original_list.copy())
sorted_merge = merge_sort(original_list.copy())
sorted_quicksort = quicksort(original_list.copy())

# Create binary search tree
bst = None
for num in original_list:
    bst = insert(bst, num)

# Print the results
print("Original List:")
print(original_list)

print("Selection Sort:")
print(sorted_selection)

print("Merge Sort:")
print(sorted_merge)

print("Quicksort:")
print(sorted_quicksort)
print("Quicksort Tree:")
print(draw_quicksort_tree(sorted_quicksort))

print("Binary Search Tree:")
inorder(bst)
print("\n Binary Tree:")
print(draw_binary_tree(bst))

