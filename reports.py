def read_reports(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    reports = []
    for line in lines:
        row = list(map(int, line.strip().split()))
        reports.append(row)

    return reports


def increasing(numbers):
    if len(numbers) < 2:
        return True

    for i in range(1, len(numbers)):
        if numbers[i] <= numbers[i - 1]:
            return False

    return True


def decreasing(numbers):
    if len(numbers) < 2:
        return True

    for i in range(1, len(numbers)):
        if numbers[i] >= numbers[i - 1]:
            return False

    return True


def difference_test(report):
    for i in range(1, len(report)):
        diff = abs(report[i] - report[i - 1])
        if diff < 1 or diff > 3:
            return False
    return True


def increase_decrease_safe_test(report):
    return increasing(report) or decreasing(report)


def main():
    reports_list = read_reports("2-input.txt")
    safe_count = sum(
        1
        for report in reports_list
        if increase_decrease_safe_test(report) and difference_test(report)
    )
    print(safe_count)


if __name__ == "__main__":
    main()
