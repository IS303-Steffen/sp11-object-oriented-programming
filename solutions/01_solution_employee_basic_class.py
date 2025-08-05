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
1. Write an Employee class with an __init__ method that stores three
   instance variables: name, title, and salary.
2. Create two Employee objects and assign any values you like.
3. Print each employee's details in the format:
   Name: <name>, Title: <title>, Salary: <salary>
'''

# Here is one potential solution. Remember there are often many different
# ways to solve a problem, so your solution may not look exactly the same.

class Employee:
    def __init__(self, name, title, salary):
        self.name = name
        self.title = title
        self.salary = salary

    def info(self):
        return f"Name: {self.name}, Title: {self.title}, Salary: {self.salary}"

emp1 = Employee("Alice", "Manager", 80000)
emp2 = Employee("Bob", "Analyst", 60000)
print(emp1.info())
print(emp2.info())
