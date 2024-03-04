import csv

# Replace these paths with your actual file paths
locations_file_path = "Data/locations.csv"
distances_file_path = "Data/distance.csv"

# Read locations from the locations CSV file
with open(locations_file_path, 'r') as locations_file:
    locations_reader = csv.reader(locations_file)
    locations = [row[2] for row in locations_reader]  # Assuming the location is in the third column

# Read distances from the distances CSV file
with open(distances_file_path, 'r', encoding='utf-8-sig') as distances_file:  # Add 'encoding' parameter to handle BOM
    distances_reader = csv.reader(distances_file)
    # Skip the first row if it contains the BOM marker
    if distances_file.read(1) == '\ufeff':
        next(distances_reader)
    distances_matrix = [[float(value) if value and value != 'inf' else float('inf') for value in row] for row in distances_reader]

# Number of locations
num_locations = len(locations)

# Initialize an empty adjacency matrix with zeros
adjacency_matrix = [[0.0] * num_locations for _ in range(num_locations)]

# Fill the adjacency matrix with distances
for i in range(num_locations):
    for j in range(num_locations):
        adjacency_matrix[i][j] = distances_matrix[i][j]

# Print the adjacency matrix
for row in adjacency_matrix:
    print(row)
