def total_distance(left_list, right_list):
    # Sort both lists
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)
    
    # Calculate the total distance
    total_distance = 0
    for left, right in zip(left_sorted, right_sorted):
        total_distance += abs(left - right)
    
    return total_distance