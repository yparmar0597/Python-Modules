### Constructor Example

class Person:

    def __init__(self, name, age, profession):
        self.NAME = name
        self.AGE = age
        self.PROFESSION = profession

    def say_hello(self):
        print("Hello my name is {} and my profession is {}.".format(self.NAME, self.PROFESSION))

    def say_age(self):
        print("Hello my age is {}".format(self.AGE))        


obj = Person('Yash', '26', 'Software developer')
obj.say_hello()
obj.say_age()