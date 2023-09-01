class Person:

    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is ', self.name)

p = Person('Alex')
p.say_hi()

Person('Alex').say_hi()