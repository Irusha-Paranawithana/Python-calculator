#addition method
def add(x,y):
    return x+y
#subtraction method
def subtract(x,y):
    return x-y
#multiplication method
def multiply(x,y):
    return x*y
#division method
def division(x,y):
    return x/y
#Prompting the options
print("Select operation.")
print("1->Add")
print("2->Subtract")
print("3->Multiply")
print("4->Divide")

while True:
    #input the operation from the user
    option = input("Enter choice(1/2/3/4):")

    #if type "end", end the process
    if option == "end":
        break
    else:
    #input the numbers to do the sum from the user
        num1 = float(input ("Enter First Number:"))
        num2 = float(input ("Enter Second Number:"))

   #filtering and performing the operation
    if option == '1':
        print("The answer is :",add(num1,num2))
    elif option == '2':
        print("The answer is :",subtract(num1,num2))
    elif option == '3':
        print("The answer is :",multiply(num1,num2))
    elif option == '4':
        print("The answer is :",division(num1,num2))
    else:
        print("Enter a valid number")       
