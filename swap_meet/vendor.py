
class Vendor:
    def __init__(self, inventory = None):
        self.inventory = [] if inventory is None else inventory
        
    def add(self, new_item):
        self.inventory.append(new_item)
        return new_item

    def remove(self, removed_item):
        if removed_item not in self.inventory:
            return False
        self.inventory.remove(removed_item)
        return removed_item

    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item             
        return None

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        self.inventory.remove(my_item)
        other_vendor.inventory.append(my_item)
        self.inventory.append(their_item)
        other_vendor.inventory.remove(their_item)
        return True
    
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        self.inventory[0], other_vendor.inventory[0] = other_vendor.inventory[0], self.inventory[0]
        return True

    def get_by_category(self, category):
        item_list = []
        for item in self.inventory:
            if item.get_category() == category:
                item_list.append(item)
        return item_list

        
    def get_best_by_category(self, category):
        item_list = self.get_by_category(category)
        if not item_list:
            return None 
        
        best_item = item_list[0]
        for item in item_list:
            if item.condition > best_item.condition:
                best_item = item
        return best_item


    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_wanted_item = other_vendor.get_best_by_category(my_priority)
        their_wanted_item = self.get_best_by_category(their_priority)

        if my_wanted_item is None or their_wanted_item is None:
            return False
        
        return self.swap_items(other_vendor, their_wanted_item, my_wanted_item)

    
    # def swap_by_newest(self, other_vendor):
    #     if not self.inventory or not other_vendor.inventory:
    #         return False
    #     my_newest = min(self.age) 
    #     other_newest = min(other_vendor.age)
    #     return self.swap_items(self, other_vendor, my_newest, other_newest)
