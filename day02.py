def is_safe(report):
    if not report:
        return False

    increasing = decreasing = True

    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]
        if not (1 <= abs(diff) <= 3):
            return False
        if diff > 0:
            decreasing = False
        elif diff < 0:
            increasing = False

    return increasing or decreasing

def is_safe_with_dampener(report):
    if len(report) < 2:
        return True

    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report):
            return True

    return False

def count_safe_reports(file_path):
    with open(file_path, 'r') as file:
        reports = file.readlines()

    safe_count = 0
    for report in reports:
        levels = list(map(int, report.strip().split()))
        if is_safe(levels) or is_safe_with_dampener(levels):
            safe_count += 1

    return safe_count

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("Usage: python report.py <file_path>")
    else:
        file_path = sys.argv[1]
        result = count_safe_reports(file_path)
        print(result)
