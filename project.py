operation = input ("Choose your operation")
     
x = input ("What is your first number?")
y = input ("What is your second number?")

def add(x,y):
    answer = (int(x)+int(y))
    return (answer)

def sub(x,y):
    answer = (int(x)-int(y))
    return (answer)
    
    
if operation == "addition" or operation == "add":
    message = "Your sum is " + str(add(x,y))
    
elif operation == "subtraction" or operation == "subtract":
    message = "Your difference is " + str(sub(x,y))
else:
    message = "Invalid input"

print (message)

