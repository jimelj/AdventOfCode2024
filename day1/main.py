# part1
# from pathlib import Path
# from totalDistance import total_distance

# def read_data(file_path):
#     # Read the data from the file
#     left_list = []
#     right_list = []
#     with file_path.open('r') as file:
#         for line in file:
#             # Split the line into two numbers
#             left, right = map(int, line.split())
#             left_list.append(left)
#             right_list.append(right)
    
#     return left_list, right_list

# # Define the path to the input file
# file_path = Path("input/example.txt")

# # Read sample data from the txt file
# left_list, right_list = read_data(file_path)

# # Calculate the total distance
# result = total_distance(left_list, right_list)

# # Print the result
# print("Total distance:", result)

from pathlib import Path
from collections import Counter

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

def calculate_similarity_score(left_list, right_list):
    # Count the occurrences of each number in the right list
    right_count = Counter(right_list)
    
    # Calculate the similarity score
    similarity_score = 0
    for num in left_list:
        similarity_score += num * right_count[num]
    
    return similarity_score

# Define the path to the input file
file_path = Path("input/input.txt")

# Read sample data from the txt file
left_list, right_list = read_data(file_path)

# Calculate the similarity score
similarity_score = calculate_similarity_score(left_list, right_list)

# Print the result
print("Similarity score:", similarity_score)