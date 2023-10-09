def sort_underscore_students(student_list):
  sorted_students = sorted(student_list, key=lambda x: x['CGPA'], reverse=True)
  return sorted_students


students = [
    {
        'name': 'jack',
        'CGPA': 0.5
    },
    {
        'name': 'rose',
        'CGPA': 0.6
    },
    {
        'name': 'dhyara',
        'CGPA': 0.7
    },
    # Add more student objects as needed
]

sorted_students = sort_underscore_students(students)

for student in sorted_students:
  print(f"Name: {student['name']}, CGPA: {student['CGPA']}")
