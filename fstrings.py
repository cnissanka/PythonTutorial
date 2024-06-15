''' 
 F-Strings
'''

name:str = "Alice" 
age:int = 25 
location:str = "UK" 

message:str = f"Hi my name is {name}, I live in {location} and my age is {age}." 

n1:int = 5 
n2:int = 7 

message2:str = f"{n1} + {n2} = {n1+n2}."
print(message2)

import math 

# multi-line
message = f"""
Name    : {name}
Location: {location}
Age     : {age}
"""
# print(f"The value of pi is approximately {math.pi:.1f}.") 

print(message)

# currencies 
amount = 123456.789
formatted_amount = f"${amount:,.2f}"
print(formatted_amount)  # Output: $123,456.79