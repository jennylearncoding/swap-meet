from swap_meet.item import Item

class Electronics(Item):

    def __init__(self, id = None, condition = 0, type = "Unknown"):
        super().__init__(id = id, condition = condition)
        self.type = type
    
    def __str__(self):
        electronics_msg = f" This is a {self.type} device."
        return super().__str__() + electronics_msg
