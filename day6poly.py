class animal:
    def speak():
        return"speaking-------"
class dog(animal):
    def speak():
        return"dog is speaking--------"
class puppy(dog):
    def speak():
        return"puppy is speaking-------"
obj3=puppy
print(obj3.speak())