# Simple Python Program - Student Grade Calculator
# This program calculates and displays student grades with statistics

def calculate_grade(score):
    """Convert numerical score to letter grade"""
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# Student data
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
    {"name": "Diana", "score": 95}
]

# Calculate and display results
print("Student Grade Report")
print("-" * 30)

total_score = 0
for student in students:
    grade = calculate_grade(student["score"])
    print(f"{student['name']}: {student['score']} ({grade})")
    total_score += student["score"]

# Calculate and display average
average = total_score / len(students)
print(f"\nClass Average: {average:.1f} ({calculate_grade(average)})")
print(f"Total Students: {len(students)}")