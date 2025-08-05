'''
OPTIONAL AI GUIDANCE PROMPT
---------------------------
I am a student in an introductory Python class. I am learning many coding
principles for the very first time. I am going to paste in the instructions
to a practice problem that my professor gave me to try before class.
Please be my kind tutor and walk me through how to solve the problem step
by step.

Don't just give me the full solution all at once (unless I later ask for
it). Instead, help me work through it gradually, with clear explanations
and small, easy-to-understand examples. Please use everyday language and
explain things in a simple, friendly way.

INSTRUCTIONS:
-------------
1. Create a Student class with id_num, name, and gpa.
2. Instantiate three Student objects and store them in a dictionary
   where the key is id_num and the value is the Student object.
3. Prompt for an id, look up the student, and print the student's GPA.
'''

# Here is one potential solution. Remember there are often many different
# ways to solve a problem, so your solution may not look exactly the same.

class Student:
    def __init__(self, id_num, name, gpa):
        self.id_num = id_num
        self.name = name
        self.gpa = gpa

registry = {
    1: Student(1, "Ana", 3.9),
    2: Student(2, "Ben", 3.5),
    3: Student(3, "Cal", 3.7)
}
lookup = int(input("Enter student ID: "))
student = registry.get(lookup)
if student:
    print(f"{student.name}'s GPA: {student.gpa}")
else:
    print("Student not found")
