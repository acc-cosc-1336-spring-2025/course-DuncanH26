#
import unittest
from src.homework.i_dictionaries_sets import add_inventory
from src.homework.i_dictionaries_sets import remove_inventory_widget

class Test_Config(unittest.TestCase):

    def test_add_inventory(self):
        inventory = {}
        add_inventory(inventory, 'Widget1', 10)
        expected_inventory = {'Widget1': 10}

        self.assertEqual(inventory, expected_inventory)
       
        add_inventory(inventory, 'Widget1', 25)
        expected_inventory = {'Widget1': 35}

        self.assertEqual(inventory, expected_inventory)

        add_inventory(inventory, 'Widget1', -10)
        expected_inventory = {'Widget1': 25}

        self.assertEqual(inventory, expected_inventory)


    def test_remove_inventory(self):

        inventory = {}

        add_inventory(inventory,'Widget1', 5)
        add_inventory(inventory, 'Widget2', 10)

        result = remove_inventory_widget(inventory, 'Widget1')

        self.assertEqual(len(inventory), 1)
        self.assertEqual('Widget2', inventory)






        

        




        
