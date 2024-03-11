import random
class MagicalHat: #a magical hat that assigns a house randomly to a person
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod 
    def assign(cls, name):
        print(name, "is in", random.choice(cls.houses))


MagicalHat.assign("Harry")


'''
@classmethod is used to define a method that takes 'cls' as the first input it works with the class itself rather than creating an instance of the class
'''