""" Sample problem featuring the builder pattern. """

import unittest

from test_context import Pizza

class TestPizza(unittest.TestCase):
    """ Tests the Pizza class """

    def test_init(self):
        """ Tests the constructor of the Pizza class """
        test_pizza = Pizza()
        self.assertIsNone(test_pizza.crust)
        self.assertIsNone(test_pizza.cheese)
        self.assertIsNone(test_pizza.pepperoni)
        self.assertIsNone(test_pizza.mushrooms)
        self.assertIsNone(test_pizza.onions)
        self.assertIsNone(test_pizza.sausage)
        self.assertIsNone(test_pizza.bacon)
        self.assertIsNone(test_pizza.peppers)

if __name__ == '__main__':
    unittest.main()
