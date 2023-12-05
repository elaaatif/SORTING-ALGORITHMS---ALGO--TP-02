import graphviz

def generate_png_from_dot(dot_file_path, png_file_path):
    # Read the DOT file
    with open(dot_file_path, 'r') as dot_file:
        dot_data = dot_file.read()

    # Create a Graph from the DOT data
    graph = graphviz.Source(dot_data)

    # Save the graph as a PNG file
    graph.render(png_file_path, format='png', cleanup=True)

if __name__ == "__main__":
    dot_file_path = "quicksort_tree.dot"
    png_file_path = "quicksort_tree.png"

    generate_png_from_dot(dot_file_path, png_file_path)
    print(f"PNG file generated: {png_file_path}")
