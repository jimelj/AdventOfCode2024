from pathlib import Path
from totalDistance import total_distance

def read_data(file_path):
    # Read the data from the file
    left_list = []
    right_list = []
    with file_path.open('r') as file:
        for line in file:
            # Split the line into two numbers
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
    
    return left_list, right_list

# Define the path to the input file
file_path = Path("input/input.txt")

# Read sample data from the txt file
left_list, right_list = read_data(file_path)

# Calculate the total distance
result = total_distance(left_list, right_list)

# Print the result
print("Total distance:", result)