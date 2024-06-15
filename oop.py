# class Dog:
#     def __init__(self, name:str, age:int):
#         self.name = name 
#         self.age = age 
    
#     def bark(self):
#         print(f"Dog {self.name} says hello"); 

# my_dog = Dog("Rex", 2) 
# my_dog.bark()


class Person:
    def __init__(self, ssn:str, name:str, creditcardNo:str):
        self.__ssn = ssn  # private 
        self.name = name  # public
        self.__creditCardNo = creditcardNo # private 

    def greet(self):
        return f"Hello my name is {self.name}" 

    def getCreditCardNumber(self, person): 
        if (person.name == "Fred"):
            return f"My credit card number is {self.__creditCardNo}."   
        else:
            return f"Sorry, I can't share my credit card number" 

personAlex = Person("SSN123213", "Alex", "645234234")  
personFred = Person("SSN2312312", "Fred", "54344344") 
personAlice = Person("SSN231312", "Alice", "2112313") 

print(personAlex.getCreditCardNumber(personAlice))

