class Person:
    def __init__(self, fn, ln, yb, salary):
        self.fb = fn
        self.ln = ln
        self.yb = yb
        self.salary = salary
        
    def new_sal(self, add_money):
        self.salary = add_money + self.salary
        return self.salary
    
    def age(self):
        return 2023 - self.yb
    
    def ten_year_sal(self):
        return self.salary * 120