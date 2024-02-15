def  add( x, y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y!=0:
        return x/y
    else:
        return "Cannot divide by zero"
    
def calculator():
    print("Simple Calculator")    
    print("1)  Addition") 
    print("2)  Subtraction") 
    print("3)  Multiplication") 
    print("4)  Division") 

    choice=input("Enter the choice:")
    if choice not in ['1','2','3','4']:
        print("Enter the valid choice ")
        return
    
    num1=int(input("Enter the first number:"))
    num2=int(input("Enter the second number:"))

    if choice=='1':
        result=add(num1,num2)
        print(result)
    elif choice=='2':
        result=subtract(num1,num2)
        print(f"The subtraction is:{num1}-{num2}={result}")
    elif choice=='3':
        result=multiply(num1,num2)
        print(f"{num1}*{num2}={result}")
    elif choice=='4':
        result=division(num1,num2)
        print(f"{num1}/{num2}={result}")

calculator()                    
    
