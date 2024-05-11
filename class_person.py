class Person:
    
    def __init__ (self, name, age, profession, nationality):
        self.name = str(name)
        self.age = int(age)
        self.profession = str(profession)
        self.nationality = str(nationality)
    def greeting(self):
        print(f"My name is {self.name}.")

    def years(self):
        print(f"He is {self.age} years old.")

    def career(self):
        print(f"He is a {self.profession}.")

    def nation(self):
        print(f"He is an {self.nationality}")

person = Person("Corc", 35, "teacher", "american")
person.greeting() 
person.years()  
person.career()
person.nation()