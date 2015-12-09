class Person:
    def __init__(self, person_name, person_age, person_country):
        self.name = person_name
        self.age = person_age
        self.country = person_country
        self.errors = []

    def checkValues(self):

        if(self.name == ""):
            self.errors.append("Your name can't be empty!")

        if(self.age < 17):
            self.errors.append("Your age can't be below 17") 

        if(self.country == ""):
            self.errors.append("Your country can't be empty!")

        return self.errors

person = Person("", -34, "")
print(person.checkValues())