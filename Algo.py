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

# Function to perform inorder traversal of binary search tree
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)

# Create three unsorted lists
list1 = random.sample(range(1, 100), 10)
list2 = random.sample(range(1, 200), 100)
list3 = random.sample(range(1, 1005), 1000)

# Apply selection sort
sorted_list1_selection = selection_sort(list1.copy())
sorted_list2_selection = selection_sort(list2.copy())
sorted_list3_selection = selection_sort(list3.copy())

# Apply merge sort
sorted_list1_merge = merge_sort(list1.copy())
sorted_list2_merge = merge_sort(list2.copy())
sorted_list3_merge = merge_sort(list3.copy())

# Create binary search trees
bst1 = None
bst2 = None
bst3 = None

for num in list1:
    bst1 = insert(bst1, num)

for num in list2:
    bst2 = insert(bst2, num)

for num in list3:
    bst3 = insert(bst3, num)

# Print the results
print("Selection Sort:")
print(sorted_list1_selection)
print(sorted_list2_selection)
print(sorted_list3_selection)

print("Merge Sort:")
print(sorted_list1_merge)
print(sorted_list2_merge)
print(sorted_list3_merge)

print("Binary Search Trees:")
inorder(bst1)
print()
inorder(bst2)
print()
inorder(bst3)
