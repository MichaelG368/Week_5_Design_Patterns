from abc import ABCMeta, abstractmethod

class Employee(metaclass=ABCMeta):
    def __init__(self, first_name, last_name, age, gender, address, SSN):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.address = address
        self.__SSN = SSN
        
    @abstractmethod
    def get_role(self):
        pass
        
    def __str__(self):
        return "{} - {} {} {} {}".format(self.__class__.__name__, self.first_name, self.last_name, self.age, self.gender)
    
class Cook(Employee):
    def get_role(self):
        return "Cook"
    
class Driver(Employee):
    def get_role(self):
        return "Driver"
    
class Manager(Employee):
    def get_role(self):
        return "Manager"
    
class EmployeeFactory(object):
    @classmethod
    def create(cls, name, *args):
        name = name.lower().strip()
        
        if name == "cook":
            return Cook(*args)
        elif name == "driver":
            return Driver(*args)
        elif name == "manager":
            return Manager(*args)
        
def main():
    cook = EmployeeFactory.create("cook", "Max", "G", 22, "M", "652 Gold Lane, New York, NY, 05278", "000-46-7532")
    driver = EmployeeFactory.create("driver", "Amy", "F", 20, "F", "652 Gold Lane, New York, NY, 05278", "000-46-7532")
    manager = EmployeeFactory.create("manager", "Rose", "F", 32, "F", "652 Gold Lane, New York, NY, 05278", "000-46-7532")
    
    print(cook)
    print(driver)
    print(manager)
    print("")
    
    print("{} is a {}.".format(cook.first_name, cook.get_role()))
    print("{} is a {}.".format(driver.first_name, driver.get_role()))
    print("{} is a {}.".format(manager.first_name, manager.get_role()))
    
main()