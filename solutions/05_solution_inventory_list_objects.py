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
1. Define a simple Product class with name and price.
2. Create at least three Product objects and store them in a list.
3. Loop through the list to calculate and print the total value of the
   inventory.
'''

# Here is one potential solution. Remember there are often many different
# ways to solve a problem, so your solution may not look exactly the same.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

items = [Product("Mouse", 20), Product("Keyboard", 30),
         Product("Monitor", 150)]
total = sum(item.price for item in items)
print(f"Total inventory value: ${total}")
