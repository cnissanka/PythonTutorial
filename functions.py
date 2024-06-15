def greetPerson(name:str="Alex", location:str="SriLanka"):
    print("Hello, ", name) 
    print("You are from ", location)

def getGreetingMessage(name:str="Alex"):
    return "Hello, " + name 

# recursion 
# function calling itself 

# f(10) = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 8 + 10
# f(2) = 1 + 2 
# f(3) = 1 + 2 + 3 
# f(1) = 1 
# def f(x:int):
#     if (x == 1):
#          return 1    
#     return x + f(x-1)
 
