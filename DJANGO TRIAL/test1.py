class Human:
    name = "Emmanuel"
    age = 30
    height = 1.74
    sex = "Male"

    def walk(you):  # Need to include 'self' as the first parameter for instance methods
        print("Walking")

    def talk(you):  # Need to include 'self' as the first parameter for instance methods
        print("Talking")

    def can_be_pregnant(you):  # Need to include 'self' as the first parameter for instance methods
        return True
    
class Male(Human):
    pass  # No need to redefine methods or attributes from the parent class

alex = Male()
print(alex.age)
