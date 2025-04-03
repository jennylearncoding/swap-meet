from swap_meet.item import Item

class Clothing(Item):

    def __init__(self, id = None, condition = 0, age = 0, fabric = "Unknown"):
        super().__init__(id=id, condition=condition)
        self.fabric = fabric
    
    
    def __str__(self):
        clothing_msg = f" It is made from {self.fabric} fabric."
        return super().__str__() + clothing_msg

