class person:
    def __init__(self, name, age,current_year):
        self.name= name
        self.age= age
        self.current_year=current_year
        #self.new_age=new_age
# Hello, my name is <name> and I am <age> years old

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old")
    def birth_year(self):
        #self.current_year= current_year
        #birth_year= current_year - self.age
        print("exact birth year is: ", self.current_year- self.age)
# Add a method update_age(new_age)
# Update the object’s age
# Call greet() again to show the change
    def is_adult(self):
        if self.age >=18:
            print("Adult")
            #print values@
        else:
            print("Minor")
    def update_age(self, new_age):
        self.age=new_age
        print(f"New age is: {self.age}")
#new

p1=person("Alex", 41, 2025)
p1.greet()
p1.birth_year()
p1.is_adult()
p1.update_age(31)