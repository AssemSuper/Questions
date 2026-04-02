class Robot_Dog:
    def __init__(self,name_val,breed_val):
        self.name=name_val
        self.breed=breed_val
    def bark(self):
        print("Woof!")
    #Main program
my_dog=Robot_Dog("Robby","Beagle")
print(my_dog.name)
print(my_dog.breed)
my_dog.bark()