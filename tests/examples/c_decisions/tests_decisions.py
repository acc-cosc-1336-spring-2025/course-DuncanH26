import unittest

from src.examples.c_decisions.decisions import test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_logical_and_truth_table(self):
        self.assertEqual(False, False and False)
        self.assertEqual(False, False and True)
        self.assertEqual(False, True and False)
        self.assertEqual(True, True and True)

