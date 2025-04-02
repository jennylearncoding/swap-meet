from swap_meet.item import Item
class Decor(Item):
    def __init__(self, id = None, condition = 0, width = 0, length = 0):
        super().__init__(id = id, condition = condition)
        self.width = width
        self.length = length

    def __str__(self):
        return f"An object of type Decor with id {self.id}. It takes up a {self.width} by {self.length} sized space."


#     - For example, if we had a `Decor` instance with an `id` of `123435`, `width` of `3`, and `length` of `7`, its stringify method should return `"An object of type Decor with id 12345. It takes up a 3 by 7 sized space."`