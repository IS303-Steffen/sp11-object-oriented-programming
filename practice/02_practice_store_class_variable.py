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
1. Extend the Employee class by adding a class variable company_name set
   to "TechCorp".
2. Create one Employee object and print company_name two ways:
   - Access through the class (Employee.company_name).
   - Access through the object (emp.company_name).
3. Change company_name via the class to "BizSoft" and print both
   accesses again so you can see the change.
'''

# starter code
class Employee:
    def __init__(self, name, title, salary):
        self.name = name
        self.title = title
        self.salary = salary

