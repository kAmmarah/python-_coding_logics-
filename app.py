print("hello world")

# Arithmetic operators
print(7 + 5)  # Addition
print(10 - 5)  # Subtraction
print(10 / 2)  # Division
print(5 * 2)  # Multiplication
print(8 ** 2)  # Exponentiation
print(11 // 2)  # Floor division
print(11 % 2)  # Modulus (remainder)

# Variable types
name: str = "Sir Ameen"  # String
age: int = 20  # Integer
is_active: bool = True  # Boolean

# Working with variables and operators
num1 = 5
num2 = 5
print(num1 + num2)  # Addition
print(num1 - num2)  # Subtraction
print(num1 / num2)  # Division
print(num1 * num2)  # Multiplication

# Assignment operators
x = 25
x = x + 5  # Add 5 to x
print(x)
x = x - 5  # Subtract 5 from x
print(x)
x = x * 2  # Multiply x by 2
print(x)
x = x % 3  # Modulus (remainder)
print(x)

# Comparison operators
num1 = 20
num2 = 11
print(num1 == num2)  # Equal to
print(num2 > num1)  # Greater than
print(num2 < num1)  # Less than
print(num1 >= num2)  # Greater than or equal to
print(num1 <= num2)  # Less than or equal to
print(num1 != num2)  # Not equal to

# Logical operators
x = True
y = False
print(x and y)  # and operator
print(x or y)  # or operator
print(not x)  # not operator

# Lists and iteration
names: list[str] = ["Sir Aneeq", "Sir Sohaib", "Sir Sami"]
numbers: list[int] = [1, 2, 3, 4, 5]

print(names[1])  # Accessing list elements
print(*range(0, 5))  # Using range

for num in numbers:
    print("num is", num)

# Simple calculator function
def calculator(num1, num2, operation):
    if operation == "addition":
        return num1 + num2
    elif operation == "subtraction":
        return num1 - num2
    elif operation == "multiplication":
        return num1 * num2
    elif operation == "division":
        if num2 == 0:
            return "Division by zero is not allowed"
        return num1 / num2
    else:
        return "Invalid operation"

#Class 1 Coding
print("Ammara")

#Class 2 :Here we will learn to Overwrite
crname="Ammara"
print(crname)

crname="M Rohaan"
print(crname)


#Variable Data Types

#Text = String
#Numbers = Integers
#True/Faise = Boolion

#bold text## First, we will use strings here
uname:str="Sir Ameen"
print(uname)

#Overwrite
#Now, I will use integers here

marks:int=80
print(marks)
age=15
print(age)
me=15
print(me)

#Boolion
allowed:bool=True
print(allowed)

allowed=False
print(allowed)

#Class 3:Here we will read the types of Operators/0perand
#Arithmetic Operator
#Assignment Operator
#Comparison Operator
#Logical Operator

#1. Arithmetic Operators (+,-,/,*)
#Addition (+)
print(7+5)

print(6+9)

num1:int=5
num2:int=5
sum:int=num1+num2
print(sum)

#Subtraction (-)
print(10-5)

num1:int=10
num2:int=9
sub:int=num1-num2
print(sub)

#Division (/)
print(25/5)

num1:int=99
num2:int=9
div:int=num1/num2
print(div)

#Multiplication (*)
print(5*7)

num1:int=2
num2:int=6
mul:int=num1*num2
print(mul)


#  Double Multiplication (**) exponent x^y
print(8**2)

num1:int=4
num2:int=2
mul:int=num1**num2
print(mul)


# This is formatted as code
#Floor Division (//) value roundoff
#List item
#List item

print(4//4)

num1:int=12
num2:int=5
div:int=num1//num2
print(div)


# **Modulas (Reminder)** (%)
print(11%2)

num1:int=7
num2:int=3
mod:int=num1%num2
print(mod)

#2. Assignment Operators (=)
#X = 5  ( Veriable = Value )

x:int=10
# 10 + 5 = 15
x=x+5
print(x)

# here, I will overwrite
# x:int=15
# x=x%3
x=15%3
print(x)

#3. Comparision Operators
#(==) Equal to
#(>) Greater than
#(<) Less than
#(>=) Greater than or Equal to
#(<=) Less than or Equal to
#(!=) not Equal to

# Comoarison Operators give out put in boolion
num1:int=10
num2:int=10
print(num1==num2)

num=10
num2=20
print(num2>num1)
print(num2<num1)

num1=10
num2=10
print(num1!=num2)


#Class 4
#4. Logical Operators (and,or,not)

# **and**
#**(all conditions should be true )**
num1:int=20
num2:int=11
print(num1>10 and num1<30)

num1=40
print(num1>10)
print(num1>20)
print(num1<30)
(print(num1>10 and num1>20 and num1<30))

## or
#**( any one condition should be true )**
num1:int=40
print(num1>10 or num1<40)

num1=56
num2=30
print(num2==num1 or num1<num2)

print(num1>=num2 or num2==num1)

#not
#in this we falsify the condition
num1:int=4
num2:int=10
print(not(num1<num2))

print(not(num2==num1))

#Assignment Class 4
electric:bool="electric"
ups:bool="ups"
print(electric==ups and ups==electric)

print(electric!=ups or ups==electric)
 
 #If , else
#If ( all condition should be true )ù

if 2>1:
    print("hello")

num1 = 2
if num1<3:
  print("hi sir")





strname:str="Ameen"
age:int=20
is_active:bool=True
#print=sir Ameen


marks:int=30
print(marks)


age:int=20

#and,or,not

#num1:int=20
#num2:int=11
#condition
#num1is greator than 30
#and
#num1 is is than 10
#num>10=true
#num<30=false
#true and false
#num1:int=40
#print(num1>10 and num1<40)
#_electric  = True
#ups = False
#print(k_electric==ups)


#num:int = 10
#print (num < 10)

#if num > 0: 
   # print("number is positive")
#else:
    #print("number d negative")
    

    #if True: 
    #print("number is positive")
#else:
   # print("number d negative")

num:int = 100
if num > 0 and num > 100:
    print(" number is psitive")
 #   if: 
   # print("number is positive")
#else:
   # print("number d negative")


 #name: str = 'sir sohaib'
#if name == "sir sohaib":
 # print(" welcome sie sohaib") #intendation
#else:
   #print("app kon")
#print("kesy hn ap")

#snake case
time_of_day: str = "Afternoon"

if time_of_day == "Good Morning":
  print("Good Morinig")
elif time_of_day == "Afternoon":
   print("Good Afternoon")
elif time_of_day == "Evening":
   print("good evning")
else:
   print("Good Night")

 #string
   #integer
   #boolion
   #list

name = "Sir Ali"

names =  ["sir Aneeq"," Sir Sahaib","Sir sami"]
print(names)
name = "Sir Ali"
# 0 firt name , 1 secod name, 2 third name

names:list[str] =  ["sir Aneeq"," Sir Sohaib","Sir sami", 1,2,3, True,False]
numbers: list[int] = [1,2,3,4,5]
#print (list)
#numbers[0]>1 
#print(names)
print(names[1]) # if we use the nmber than the data is fatch and this is string
#range(0,5)
#starting point
#condition 
#increment jab first nm we right than second number how many ahve incremint 
#range(0,5)
print(*range(0,5))
print(*range(1,5))
#print(*list[range(1,5)])
#print(*list[range(1,5)])

#print(numbers[0])
#print(numbers[1])
#print(numbers[2])
#print(numbers[3])
#print(numbers[4])
#itreation number list is itrable we are doing itrate 
#for variable in iterable
for num in numbers:
  print("num is", num)
#for loop

# cLass 6, 7
print("hello world")
print("Najma")

strname:str=" Sir Ameen"
age:int=20
is_active:bool=True
#print=sir Ameen


marks:int=30
print(marks)


age:int=20

#and,or,not

#num1:int=20
#num2:int=11
#condition
#num1is greator than 30
#and
#num1 is is than 10
#num>10=true
#num<30=false
#true and false
#num1:int=40
#print(num1>10 and num1<40)
#_electric  = True
#ups = False
#print(k_electric==ups)


#num:int = 10
#print (num < 10)

#if num > 0: 
   # print("number is positive")
#else:
    #print("number d negative")
    

    #if True: 
    #print("number is positive")
#else:
   # print("number d negative")

num:int = 100
if num > 0 and num > 100:
    print(" number is psitive")
 #   if: 
   # print("number is positive")
#else:
   # print("number d negative")

 #name: str = 'sir sohaib'
#if name == "sir sohaib":
 # print(" welcome sie sohaib") #intendation
#else:
   #print("app kon")
#print("kesy hn ap")

#snake case
time_of_day: str = "afternoon"

if time_of_day == "Good Morning":
  print("Good Morinig")
elif time_of_day == "Afternoon":
   print("Good Afternoon")
elif time_of_day == "Evening":
   print("good evning")
else:
   print("Good Night")



#string
   #integer
   #boolion
   #list

name = "Sir Ali"

names =  ["sir Aneeq"," Sir Sahaib","Sir sami"]
print(names)



name = "Sir Ali"
# 0 firt name , 1 secod name, 2 third name

names:list[str] =  ["sir Aneeq"," Sir Sohaib","Sir sami", 1,2,3, True,False]
numbers: list[int] = [1,2,3,4,5]
#print (list)
#numbers[0]>1 
#print(names)
print(names[1]) # if we use the nmber than the data is fatch and this is string
#range(0,5)
#starting point
#condition 
#increment jab first nm we right than second number how many ahve incremint 
#range(0,5)
print(*range(0,5))
print(*range(1,5))
#print(*list[range(1,5)])
#print(*list[range(1,5)])

#print(numbers[0])
#print(numbers[1])
#print(numbers[2])
#print(numbers[3])
#print(numbers[4])
#itreation number list is itrable we are doing itrate 
#for variable in iterable
for num in numbers:
  print("num is", num)
#for loop


#  #range function/ method
# number = [1,2,3,4,5,6,7,8,9]
# X = range(1,10) #1,2,3,4,5
# #1. starting point.
# #2.condition mesan number kahan tak cahye 
# #3. Increment starting by defaulty 0 but after jo value hy woh uthaye ga 
# print(number)
# print(list(X)) 

#num:  int = 2
#print("2 x 1 =", num * 1)
#print("2 x 1 =", num * 2)
#print("2 x 1 =", num * 3)
#print("2 x 1 =", num * 4)
#print("2 x 1 =", num * 5)
#print("2 x 1 =", num * 6)
#print("2 x 1 =", num * 7)
#print("2 x 1 =", num * 8)
#print("2 x 1 =", num * 9)
#print("2 x 1 =", num * 10)

for num in range(1,10): #1,2,3,4,5.6.7
    #print("num is", num)  # intentation ,loops, fstring
     #print("2 x", num, "=", 2*num)
     #print(f"2 x {num} = {2 * num}") #"f" string

# loops
# 1. for loop
# 2. while loop

#num = 1
#while num <= 10:
    #print(num)
    #num = num + 1


#  start = 1
# while start<=10:
#     print(f"conut  {start}")
#     #start = start + 1
#     start +=1
# while num < 10:
#     #num = 1
#     num = num + 1
#     print(" num firts time", num)
#     #num = num + 1
#     print("num second time", num)
#     print(num)
    #print{num , 10}
    # while condition
    # while 10 < 10:
    #    print("number befor incriment", num) 
    #    num = num = + 1
    #    print("number befor incriment", num)

#  password: str ="python123"
#  user_input: str = ""

# print("user_Input")
# while user
# print("incorrect ")

 #number = [1,2,3,4,5]
#   0,    1,     2,  3,
 names1 = ["Ali", "Bilal", "Humza", "Okasa"] # List

names2 = ("Ali", "Bilal","ummar")# tripple
print("names1 is" , names1[0])
print("names1 is" , names2[0])

name: str = "Ali"
name = "Bilal"
print("names1 before overide", names1)
#print(name)
# Alia and Abdullah
names1[0] = "Abdullah"
print("names1 after overide", names1)

#number = [1,2,3,4,5]
#   0,    1,     2,  3,
names1 = ["Ali", "Bilal", "Humza", "Okasa"] # List

names2 = ("Ali", "Bilal","ummar")# tripple
print("names1 is" , names1[0])
print("names1 is" , names2[0])

name: str = "Ali"
name = "Bilal"

print("names1 before over write", names1)
#print(name)
# Alia and Abdullah
names1[1] = "Abdullah"
print("names1 after over write", names1)

#list mutable for list change 
#tuple  imutable
#key value pair the  both is important 

# #my_dict = {"Ali" 0: } we are suing both name or number 
# my_dict = {
#     "Ali":109878,
#     "Ahmed": 8899,
#     "fastima": 8899,
#            }
# #   key : value


# print(my_dict["Ahmed"])

#contact = []

#data type
# 1. string
# 2. integer
# 3.bolian
# 4.list
# 5.tupple
# 6.dictionary

#student = ["ali abdullah", ] #this is called list noyt dictionary 
# Student = {
#     "Name" : "Ali",
#     "Age" : 20,
#     "class" : " Sunday 7-10",
#     "rollno": 9886
# }

# #print(Student["Age"])
# #print(Student[0])
# print("before",Student)
# Student["Rollno"] = 9886
# print("before",Student)

# its called function for charger 
# def charger():
#     print("mobile charger")

# charger()
# def ramo_kaka(): #under snake ---> '-' 
#      #statment
#     print("Ramo Kaka Baryani Banao")  
# # bilten function mits called method 
# ramo_kaka()

# a = 1
# a = 4


# def ramokaka():
#    return "Birayani ban gai"


# plate = ramokaka
# print(plate)

#satic funcation
#dynamic function
def greet(name,age): #  parameter
    print("Asslam Alaikum sir", name, "your age is", age)

# argument 
greet(23, "bilal")
num1: int =10
num2: int = 10

def addition(): 
    print(num1+num2)

addition() 

def addition(num1 = int, num2 = int):
    print(num1+num2)

addition(10,10)

def addition(num1: int, num2 : int):
    return num1 + num2
print(addition(10,10))

result = addition(10, 10)
print("result")
finnal_result = result + 20
print(finnal_result)


#Calculator

def calculator(num1, num2, operation):
    if operation == "addition":
        return num1 + num2
    elif operation == "subtraction":
        return num1 - num2
    elif operation == "multiplication":
        return num1 * num2
    elif operation == "division":
        if num2 == 0:
            return "Division by zero is not allowed"
        return num1 / num2
    else:
        return "Invalid operation"

# Main program
def main():
    print("Welcome to my Python calculator")
    
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        print("Choose the operation: Addition, Subtraction, Multiplication, Division")
        operation = input("Enter the operation: ").strip().lower()

        result = calculator(num1, num2, operation)

        print(f"The result of {operation} is: {result}")

        cont = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if cont != "yes":
            print("Thank you for using the calculator. Goodbye!")
            break

main()


