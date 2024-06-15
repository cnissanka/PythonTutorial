'''
 Inheritance and Polymorphism 
''' 

class Greeting: 
    
    def __init__(self, name:str):
        self.name = name 
    
    def sayGreeting(self):
        raise NotImplementedError("Subclasses must implement this abstract method") 

class AsianGreeting(Greeting):

    def sayGreeting(self):
        return f"Nǐ hǎo {self.name}"

class WesternGreeting(Greeting):

    def sayGreeting(self):
        return f"Hello, {self.name}" 


def greetMe(greetingObj):
    return greetingObj.sayGreeting() 


asian_greeting = AsianGreeting("Alex") 
western_greeting = WesternGreeting("Alex") 

print(greetMe(western_greeting))