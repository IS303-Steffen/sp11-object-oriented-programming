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
1. Create a Product class that stores name and price.
2. Add an instance method apply_discount(self, percent) that lowers the
   price by percent (e.g., 10 gives a 10% discount) and returns the new
   price.
3. Create one Product priced at $50, apply a 20% discount, and print the
   new price.
'''

# Here is one potential solution. Remember there are often many different
# ways to solve a problem, so your solution may not look exactly the same.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self, percent):
        self.price *= (1 - percent/100)
        return self.price

p = Product("Headphones", 50)
print("Discounted price:", p.apply_discount(20))
