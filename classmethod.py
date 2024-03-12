import random
class MagicalHat: #a magical hat that assigns a house randomly to a person
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod 
    def assign(cls, name):
        print(name, "is in", random.choice(cls.houses))


MagicalHat.assign("Harry")


'''
@classmethod takes the first input as cls, and functions defined with @classmethods are tied to the class itself, rather than its instances,they can excess modify class-level attributes and call other methods too : it is used when when we do not need any obj of the class
'''