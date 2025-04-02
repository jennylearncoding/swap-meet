### Wave 2

# In Wave 2 we will create the `Item` class and the `Vendor` class' `get_by_id` method.


from uuid import uuid4
class Item:
    def __init__(self, id = None):
        self.id = id if id is not None else uuid4().int
    
    def get_category(self):
        return self.__class__.__name__

    def __str__(self):
        return f"An object of type Item with id {self.id}."
