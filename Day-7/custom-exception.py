# You can make a custom Exception like this. We will cover it in Classes indepth.
class Salarynotinrangeerror(Exception):
    def __init__(self, salary, message="Salary is not in (5000, 10000) range"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)


salary = int(input("Enter the Salary Amount: "))
if not 5000 < salary < 10000:
    raise Salarynotinrangeerror(salary)
