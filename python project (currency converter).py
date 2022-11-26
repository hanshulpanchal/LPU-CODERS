print("Welcome to the currency converter")
n = "y"
while n=="y":
    a = input("Name the currency to be converted from: ")
    b = input("Name the currency to be converted into: ")
    c = int(input("Amount of "+a+" to be converted: "))
    d = float(input("How many "+b+" is one "+a+": "))
    print("That would be",c*d,b)
    n=input("Would you like to continue??(y/n): ")
print("Thank you, This was made by: \n Hanshul(23)\n Himanshu(24)\n Aditya Pathania(25)")
