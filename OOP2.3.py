class Employee:
    def __init__(self, name, position, salary, hierarchy):
        self.name = name
        self.position = position
        self.salary = salary
        self.hierarchy = hierarchy

    def print_info(self):
        print(f'Name: {self.name}, Position: {self.position}, Salary: {self.salary}, Position: {self.hierarchy}')


class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, 'Manager', salary, "Upper")


class Engineer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, 'Engineer', salary, "Middle")
        self.programming_language = programming_language

    def print_info(self):
        super().print_info()
        print(f'Programming Language: {self.programming_language}')


class Salesman(Employee):
    def __init__(self, name, salary, sales_volume):
        super().__init__(name, 'Salesman', salary, "Middle")
        self.sales_volume = sales_volume

    def print_info(self):
        super().print_info()
        print(f'Sales Volume: {self.sales_volume}')


class Designer(Employee):
    def __init__(self, name, salary, design_tools):
        super().__init__(name, 'Designer', salary, "Lower")
        self.design_tools = design_tools

    def print_info(self):
        super().print_info()
        print(f'Design Tools: {self.design_tools}')


class Accountant(Employee):
    def __init__(self, name, salary, certification):
        super().__init__(name, 'Accountant', salary, "Middle")
        self.certification = certification

    def print_info(self):
        super().print_info()
        print(f'Certification: {self.certification}')


class HumanResources(Employee):
    def __init__(self, name, salary, experience_years):
        super().__init__(name, 'Human Resources', salary, "Lower")
        self.experience_years = experience_years

    def print_info(self):
        super().print_info()
        print(f'Experience Years: {self.experience_years}')


manager = Manager('John Smith', 150000)
engineer = Engineer('Bob Johnson', 160000, 'Python')
salesman = Salesman('Alice Brown', 140000, 100000)
designer = Designer('Mary Davis', 150000, 'Adobe Photoshop, Sketch')
accountant = Accountant('Tom Wilson', 145000, 'CPA?')
human_resources = HumanResources('Emily Jones', 140000, 5)

manager.print_info()
engineer.print_info()
salesman.print_info()
designer.print_info()
accountant.print_info()
human_resources.print_info()