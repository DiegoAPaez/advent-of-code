def count_safe_reports_red_nosed(file_path):
    def is_safe_report(report):
        # Check if the levels are all increasing or all decreasing
        increasing = all(0 < report[i+1] - report[i] <= 3 for i in range(len(report) - 1))
        decreasing = all(0 < report[i] - report[i+1] <= 3 for i in range(len(report) - 1))
        return increasing or decreasing

    # Read the input file and parse the reports
    safe_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            # Convert the line into a list of integers
            report = list(map(int, line.split()))
            # Check if the report is safe and update the count
            if is_safe_report(report):
                safe_count += 1
    
    print("Red-Nosed Reports safe reports:", safe_count)

count_safe_reports_red_nosed('data_files/data_day2.txt')

def count_safe_reports_dampener(file_path):
    def is_safe_report(report):
        # Check if the levels are all increasing or all decreasing
        increasing = all(0 < report[i+1] - report[i] <= 3 for i in range(len(report) - 1))
        decreasing = all(0 < report[i] - report[i+1] <= 3 for i in range(len(report) - 1))
        return increasing or decreasing

    def can_be_safe_with_dampener(report):
        # Test removing each level one by one
        for i in range(len(report)):
            # Create a modified report without the i-th level
            modified_report = report[:i] + report[i+1:]
            # Check if the modified report is safe
            if is_safe_report(modified_report):
                return True
        return False

    # Read the input file and parse the reports
    safe_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            # Convert the line into a list of integers
            report = list(map(int, line.split()))
            # Check if the report is safe or can be made safe with the dampener
            if is_safe_report(report) or can_be_safe_with_dampener(report):
                safe_count += 1
    
    print("Problem Dampener safe reports:", safe_count)

count_safe_reports_dampener('data_files/data_day2.txt')