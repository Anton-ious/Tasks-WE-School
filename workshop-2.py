print("==========================================")
print("Welcome to $$ EXCHANGE store")
print("==========================================")

USD=1
EUR=0.25
SAR=3.93

while True:
    type=input("Exchange from (USD,EUR,SAR):").strip().lower()
    #
    if (type == "USD" or type == "usd" or type == "EUR" or type == "eur" or type == "SAR" or type == "sar"):
        print("------------------------------------------------------")
    
        while True:
            #
            number=int(input("How much? "))
            #
            if (number<0 or number==0):
                print(f"You can not exchange {number} enter any positive number or greater than 0")
            #
            else:
                break
         #
        print("------------------------------------------------------")
        type2=input("Exchange to (USD,EUR,SAR):").strip().lower()
         #
        if (type2 == "USD" or type2 == "usd" or type2 == "EUR" or type2 == "eur" or type2 == "SAR" or type2 == "sar"):
           
            if (type2 == "USD" or type2 == "usd"):            
                if (type2 == type):
                    print(f"You will give {number} and you will take the same number: {number}")
                #
                else:
                    x=USD*number
                    print(f"You will give {number} and you will take {x}")
                #
            elif (type2 == "EUR" or type2 == "eur"):
                if (type2 == type):
                    print(f"You will give {number} and you will take the same number: {number}")
                #
                else:
                    x=EUR*number
                    print(f"You will give {number} and you will take {x}")
                #
            elif (type2 == "SAR" or type2 == "sar"):
                if (type2 == type):
                    print(f"You will give {number} and you will take the same number: {number}")
                #
                else:
                    x=SAR*number
                    print(f"You will give {number} and you will take {x}")
        #
        else:
            print("This convertion it is not supported now")
            break
        #
        break
    #
    else:
        print("This convertion it is not supported now")
        break



print("------------------------------------------------------")
#
type3=input("Do you need to convert again (yes/no):").strip().lower()
#
print("------------------------------------------------------")
#
while type3=="yes":
    #
    print("==========================================")
    print("Welcome to $$ EXCHANGE store")
    print("==========================================")
    #
    while True:
        type=input("Exchange from (USD,EUR,SAR):").strip().lower()
        #
        if (type == "USD" or type == "usd" or type == "EUR" or type == "eur" or type == "SAR" or type == "sar"):
            print("------------------------------------------------------")
        
            while True:
                #
                number=int(input("How much? "))
                #
                if (number<0 or number==0):
                    print(f"You can not exchange {number} enter any positive number or greater than 0")
                #
                else:
                    break
             #
            print("------------------------------------------------------")
            type2=input("Exchange to (USD,EUR,SAR):").strip().lower()
             #
            if (type2 == "USD" or type2 == "usd" or type2 == "EUR" or type2 == "eur" or type2 == "SAR" or type2 == "sar"):
            
                if (type2 == "USD" or type2 == "usd"):            
                    if (type2 == type):
                        print(f"You will give {number} and you will take the same number: {number}")
                    #
                    else:
                        x=USD*number
                        print(f"You will give {number} and you will take {x}")
                    #
                elif (type2 == "EUR" or type2 == "eur"):
                    if (type2 == type):
                        print(f"You will give {number} and you will take the same number: {number}")
                    #
                    else:
                        x=EUR*number
                        print(f"You will give {number} and you will take {x}")
                    #
                elif (type2 == "SAR" or type2 == "sar"):
                    if (type2 == type):
                        print(f"You will give {number} and you will take the same number: {number}")
                    #
                    else:
                        x=SAR*number
                        print(f"You will give {number} and you will take {x}")
            #
            else:
                print("This convertion it is not supported now")
                break
            #
            break
        #
        else:
            print("This convertion it is not supported now")
            break
            #
    type3=input("Do you need to convert again (yes/no):").strip().lower()
    if (type3=="no"):
        break
    else:
        print("This convertion doesn not supported now")



print("--------------------------\n Quistion-2 \n----------------------------")

############################ Quistion-2 ###############################################################
item=float(input("Enter number of items:"))
rate=int(input("Enter rate of tax:" "%"))   
def calculate_total():
    total=(item+rate)
    print(f"Total is {total}")
    return total
calculate_total()

print("--------------------------\n Quistion-3 \n----------------------------")
################################ Quistion-3 ##############################################
f=int(input("Enter first number:"))
s=int(input("Enter second number:"))
t=int(input("Enter third number:"))
def find():
    if (f>s and f>t):
        print(f"{f} is the largest number")
    elif (s>f and s>t):
        print(f"{s} is the largest number")
    else:
        print(f"{t} is the largest number")
find()

print("--------------------------\n Quistion-4 \n----------------------------")
################################ Quistion-4 ##############################################
class Car:
    def __init__(self, name, price, speed,color):
        self.n = name
        self.p = price
        self.s = speed
        self.c = color
    def inp():
        name = input("Enter the name of the car:")
        price = int(input("Enter the price of the car:"))
        speed = int(input("Enter the speed of the car:"))
        color = input("Enter the color of the car:")
        return name,price,speed,color 
 
name,price,speed,color = Car.inp() 
print("------------------------------------------------------")
print(f"The Name of car is {name}")
print(f"The price of the car is {price}")
print(f"The speed of the car is {speed}")
print(f"The color of the car is {color}")

