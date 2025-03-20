import csv
from collections import defaultdict


def read_grades(file_path):
    """Reads grades from a CSV file and returns a list of dictionaries."""
    grades = []
    try:
        with open(file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                grades.append({
                    'name': row['Name'],
                    'subject': row['Subject'],
                    'grade': int(row['Grade'])
                })
    except FileNotFoundError:
        print(f"Error: {file_path} not found. Please check the file path.")
    return grades


def calculate_average(grades):
    """Calculates the average grade for each subject."""
    subject_totals = defaultdict(lambda: {'total': 0, 'count': 0})

    for entry in grades:
        subject = entry['subject']
        subject_totals[subject]['total'] += entry['grade']
        subject_totals[subject]['count'] += 1

    averages = {subject: total['total'] / total['count'] for subject, total in subject_totals.items()}
    return averages


def write_averages(file_path, averages):
    """Writes average grades to a CSV file."""
    try:
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Subject', 'Average Grade'])
            for subject, avg in averages.items():
                writer.writerow([subject, round(avg, 2)])
        print(f"Average grades successfully saved to {file_path}")
    except Exception as e:
        print(f"Error writing to file: {e}")


# File paths
grades_file = 'grades.csv'
averages_file = 'average_grades.csv'

# Process grades
grades = read_grades(grades_file)
if grades:
    averages = calculate_average(grades)
    write_averages(averages_file, averages)
    print("Processing complete!")
else:
    print("No data to process.")

