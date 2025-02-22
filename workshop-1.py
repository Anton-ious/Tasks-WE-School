

x=5
y=6
print(x+y)
result=x+y
print(result)
print("Sum of",x,"+",y,"=",result)
print(f"The result is:{result}")
############################ ########################
firstname="Anton"
score=50
print(f"The score of {firstname} is {score}")
#####################################################
def sum2():
    f=int(input("Enter first number:"))
    s=int(input("Enter second1 number:"))
    r=f+s
    print(r)
sum2()
####################################################
rate=(5,4,3,2,1)
member = {
    "Ahmed": rate[0],
    "Mhamed":rate[1],
    "Hamed":rate[2]
}
# s=member+rate
# print(s)

if (member["Ahmed"] >= 5):
    print("Your rate is excelant")
elif (member["Hamed"] == 4 or 3):
    print("Your rate is good")
elif (member["Mhamed"] == 2 or 2.99):
    print("Your rate is bad")
else:
    print("Your rate is very bad")

################################################################
num=int(input("Enter multiplication table:"))
for i in range(11):
    print(num,"X",i,"=",num*i)
################################################################
q=int(input("Enter number:"))
for i in range(1,q):
    if (i % 2 ==0):
        print(i)
################################################################
x=int(input("Enter number:"))
while x > 0 :
    x-=1
    print(x)
#############################################################

o=input("Enter password:")
while o:   
    if (o != "python123"):
        print("passwordnotcorrect")
    else:
        print("password-correct")
        break
###########################################################
t=[10,20,30,40]
print(sum(t))
print(min(t))
print(max(t))
##########################################################
student={"name":"mohamed","age":12,"grade":"a"}
print("the student age is:",student["age"])
############################################################
student={"name":"mohamed","age":12,"grade":"a"}
for i in student:
    print(student)
#############################################################
car={"name":"bmw","speed":120040432,"salary":200000}
for key,value in car.items():
    print(f"{key}:{value}")