### Wave 2

# In Wave 2 we will create the `Item` class and the `Vendor` class' `get_by_id` method.


from uuid import uuid4
class Item:
    def __init__(self, id=None, condition=0, age=0):
        self.id = id if id is not None else uuid4().int
        self.condition = condition
        self.age = age

    
    def get_category(self):
        return self.__class__.__name__

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."

    def condition_description(self):
    #     descriptions = {
    #     0: "You probably want a glove for this one...",
    #     1: "Heavily used",
    #     2: "Worn but usable",
    #     3: "Gently used",
    #     4: "Like new",
    #     5: "Mint condition"}
    #     return descriptions.get(self.condition)
        if self.condition <= 1:
            return "You probably want a glove for this one..."
        elif 1 < self.condition <= 2:
            return "Heavily used"
        elif 2 < self.condition <= 3:
            return "Worn but usable"
        elif 3 < self.condition <= 4:
            return "Gently used"
        elif 4 < self.condition <= 5:
            return "Like new"
        else:
            return "Mint condition"
