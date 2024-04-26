class Human:
    name = "Emmanuel"
    age = 30
    heigth = 1.74
    sex = "Male"

    def walk(self):
        print("Walking")

    def talk(self):
        print("Talking")

    def canbepregnant(self):
        return True
    
class Male(Human):
    pass
    
alex = Male()
alex.talk()