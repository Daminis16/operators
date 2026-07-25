a = input("Enter a number 1: ")
b = input("Enter a number 2: ")

print("The sum of the two numbers is: ", a + b)
#this only concatenates the two numbers as they are treated as strings
#to perform addition we need to convert them to integers






#to convert the input to integer we can use the int() function
c = input("Enter a number: ")
d = input("Enter another number: ")

print("The sum of the two numbers is: ", int(c) + int(d))


#we can also directly convert the input to integer while taking the input
e=int(input("Enter a number: "))
f=int(input("Enter another number: "))
print("The sum of the two numbers is: ", e + f)