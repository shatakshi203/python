class University:
    def __init__(self):
        self.faculty_dict = {}
        self.students_dict = {}

    def add_faculty(self, faculty_id, name, department):
        self.faculty_dict[faculty_id] = {'Name': name, 'Department': department}

    def add_student(self, student_id, name, major):
        self.students_dict[student_id] = {'Name': name, 'Major': major}

    def display_faculty_info(self, faculty_id):
        if faculty_id in self.faculty_dict:
            print("Faculty Information:")
            print(f"ID: {faculty_id}")
            print(f"Name: {self.faculty_dict[faculty_id]['Name']}")
            print(f"Department: {self.faculty_dict[faculty_id]['Department']}")
        else:
            print(f"Faculty with ID {faculty_id} not found.")

    def display_student_info(self, student_id):
        if student_id in self.students_dict:
            print("Student Information:")
            print(f"ID: {student_id}")
            print(f"Name: {self.students_dict[student_id]['Name']}")
            print(f"Major: {self.students_dict[student_id]['Major']}")
        else:
            print(f"Student with ID {student_id} not found.")

# Example usage:
university = University()

# Adding faculty
university.add_faculty("F101", "John Doe", "Computer Science")
university.add_faculty("F102", "Jane Smith", "Physics")

# Adding students
university.add_student("S201", "Alice Johnson", "Engineering")
university.add_student("S202", "Bob Williams", "Biology")

# Displaying information
university.display_faculty_info("F101")
university.display_student_info("S201")
