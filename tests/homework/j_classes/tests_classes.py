#
import unittest
from src.homework.j_classes import roll
from src.homework.j_classes import get_rolled_value
from src.homework.j_classes import __str__
from src.homework.j_classes import die

class Test_Config(unittest.TestCase):


 def test_get_rolled_value(self):

    d = die()
    
    d.roll
    
    roll_1 = d.get_rolled_value()
    roll_2 = d.get_rolled_value()
    roll_3 = d.get_rolled_value()


    self.assertEqual(True, 1 <= roll_1 <=6)
    self.assertEqual(True, 1 <= roll_2 <=6)
    self.assertEqual(True, 1 <= roll_3 <=6)



