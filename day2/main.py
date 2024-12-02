# Part1
# def is_safe(report):
#     levels = list(map(int, report.split()))
#     diffs = [levels[i+1] - levels[i] for i in range(len(levels) - 1)]
#     return all(1 <= d <= 3 for d in diffs) or all(-3 <= d <= -1 for d in diffs)

# def count_safe_reports(file_path):
#     with open(file_path, 'r') as file:
#         return sum(is_safe(line.strip()) for line in file)

# # Input file path
# file_path = "input/input.txt"

# # Print the number of safe reports
# print("Number of safe reports:", count_safe_reports(file_path))

def is_safe(report):
    """
    Check if a report is safe based on the given conditions:
    - Levels are either all increasing or all decreasing.
    - Any two adjacent levels differ by at least 1 and at most 3.
    """
    levels = list(map(int, report.split()))
    diffs = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]
    return all(1 <= d <= 3 for d in diffs) or all(-3 <= d <= -1 for d in diffs)


def is_safe_with_dampener(report):
    """
    Check if a report is safe considering the Problem Dampener,
    which allows removing one level to make it safe.
    """
    levels = list(map(int, report.split()))
    # Check if already safe
    if is_safe(report):
        return True

    # Check if removing one level makes it safe
    for i in range(len(levels)):
        modified_report = levels[:i] + levels[i + 1:]  # Remove one level
        if is_safe(" ".join(map(str, modified_report))):
            return True

    return False


def count_safe_reports(file_path):
    """
    Counts the number of safe reports considering the Problem Dampener.
    """
    with open(file_path, 'r') as file:
        return sum(is_safe_with_dampener(line.strip()) for line in file)


# Input file path
file_path = "input/input.txt"

# Print the number of safe reports
print("Number of safe reports with Problem Dampener:", count_safe_reports(file_path))