# Printing, Commenting, Debugging, String Manipulation and Variables
# Project 01 - Create A band name generator


print("Welcome to the Band Name Generator.")

CityName = input("What's name of the city you grew up in ?" + "\n")

PetsName = input("What's your pet's name ?" + "\n")

print(f"Your band name could be {CityName} {PetsName}")

print("------------------------------------------------------------------------------")

# Project 02 - Create a calculator 

print(" Welcome to Our Calculator !!!! ")

Option = int(input("Choose Operation you want to perform " + "\n" + "1. Addition " + "\n" + "2. Subtraction" + "\n" + "3. Division" + "\n" + "4. Multiplication" + "\n"))

num1   = int(input("Enter First Number :" + "\n"))
num2   = int(input("Enter Second Number :" + "\n"))

if(Option == 1):
    print(f"Your Answer is {num1 + num2}")

elif(Option == 2):
    print(f"Your Answer is {num1 - num2}")

elif(Option == 3):
    print(f"Your Answer is {float(num1 / num2)}")

elif(Option == 4):
    print(f"Your Answer is {num1 * num2}")


# Important Notes :

print("-------------------------------------------------------------------------------")
print("If you want to print \"\" in your program you can use ' \" \" '")

# Sting Operations in python 
print("-------------------------------------------------------------------------------")
MyString = input("Enter Your String which you like to calculate length of :" + "\n")
print(f"Length of your inputed string {MyString} is {len(MyString)}")

MyLength = 0

def CalculateLength(tempString):

    count   = 0
    for char in tempString:
        count = count + 1
        

    return count

MyLength = CalculateLength(MyString)

print("My Calculated Length is : " + str(MyLength))