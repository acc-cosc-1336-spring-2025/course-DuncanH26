#

inventory = {}

def add_inventory(dictionary, widget_name, quantity):

    if widget_name not in dictionary:
        dictionary[widget_name] = quantity
    else:
        dictionary[widget_name] += quantity

        return quantity
    
def remove_inventory_widget(inventory, widget_name):


 if widget_name in inventory:
        del inventory[widget_name]
        return 'Record Deleted'
 else:
     return 'Item not found'
 

        

 