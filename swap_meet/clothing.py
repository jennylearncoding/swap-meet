from swap_meet.item import Item
 
class Clothing(Item):
 
    def __init__(self, id = None, condition = 0, age=0, fabric = "Unknown"):
        super().__init__(id=id, condition=condition, age=age)
        self.fabric = fabric
    
    def __str__(self):
        return f"{super().__str__()} It is made from {self.fabric} fabric."