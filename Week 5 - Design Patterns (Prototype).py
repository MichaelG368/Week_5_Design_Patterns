import copy

class Prototype(object):
    
    def clone(self):
        return copy.deepcopy(self)
    
class MenuItem(Prototype):
    
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
        
    def __str__(self):
        return "{} - {} (${})".format(self.name, self.description, self.price)
    
def main():
    menu_item_1 = MenuItem("Cheese Pizza", "Medium-sized pizza with cheese and tomato sauce", 14)
    print(menu_item_1)
    
    menu_item_2 = menu_item_1.clone()
    menu_item_2.name = "Pepperoni Pizza"
    menu_item_2.description = "Medium-sized pizza with cheese, pepperoni, and tomato sauce"
    menu_item_2.price = 15
    print(menu_item_2)
    
main()