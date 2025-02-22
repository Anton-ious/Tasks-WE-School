class Robot:
    def __init__(self, name,color):
        self.name= name
        self.color= color
robot= Robot('Zumba','red')
print(f"The name of the robot is {robot.name} and color is {robot.color}")

# # ---------------------------Q-2----------------------------------

class Smartphone:
    def __init__(self, brand, model):
        self.brand= brand
        self.model= model
    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

smartphone= Smartphone('Apple','iPhone 13')
smartphone.display_info()

