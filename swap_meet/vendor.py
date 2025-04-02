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
    
    def get_by_id(self, item_id):
        for item in self.inventory:
            if item.id == item_id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        self.inventory.remove(my_item)
        other_vendor.inventory.remove(their_item)
        self.inventory.append(their_item)
        other_vendor.inventory.append(my_item)
        return True


