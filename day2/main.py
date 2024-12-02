def is_safe(report):
    levels = list(map(int, report.split()))
    diffs = [levels[i+1] - levels[i] for i in range(len(levels) - 1)]
    return all(1 <= d <= 3 for d in diffs) or all(-3 <= d <= -1 for d in diffs)

def count_safe_reports(file_path):
    with open(file_path, 'r') as file:
        return sum(is_safe(line.strip()) for line in file)

# Input file path
file_path = "input/input.txt"

# Print the number of safe reports
print("Number of safe reports:", count_safe_reports(file_path))