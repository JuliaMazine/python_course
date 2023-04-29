class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def info(self):
        print(f"{self.name} is {self.age} and is studying {self.major}")

    def age_a_year(self):
        self.age += 1

class Professor:
    def __init__(self, name, faculty):
        self.name = name
        self.faculty = faculty

    def advise_student(self, student):
        print(f"{self.name} talked to {student.name} about {student.major} and why {self.faculty} is better")

    def convince_student(self, student):
        student.major = self.faculty

student1 = Student("Nadia", 19, "Mathematics")
professor1 = Professor("Savostyanov", "Fund. & App. Linguistics")

student1.info()
professor1.advise_student(student1)
professor1.convince_student(student1)
student1.age_a_year()
student1.info()








