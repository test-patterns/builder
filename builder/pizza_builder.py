""" Sample problem featuring the builder pattern. """

from pizza import Pizza

class PizzaBuilder(object):
    """ A builder for a pizza """

    def __init__(self):
        """ Initializes a new pizza builder """
        self._pizza = Pizza()

    def set_crust(self, value):
        """ Sets the crust of a pizza"""
        self._pizza.crust = value
        return self

    def set_cheese(self, value):
        """ Sets the cheese of a pizza"""
        self._pizza.cheese = value
        return self

    def set_pepperoni(self, value):
        """ Sets the pepperoni of a pizza"""
        self._pizza.pepperoni = value
        return self

    def set_mushrooms(self, value):
        """ Sets the mushrooms of a pizza"""
        self._pizza.mushrooms = value
        return self

    def set_onions(self, value):
        """ Sets the onions of a pizza"""
        self._pizza.onions = value
        return self

    def set_sausage(self, value):
        """ Sets the sausage of a pizza"""
        self._pizza.sausage = value
        return self

    def set_bacon(self, value):
        """ Sets the bacon of a pizza"""
        self._pizza.bacon = value
        return self

    def set_peppers(self, value):
        """ Sets the peppers of a pizza"""
        self._pizza.peppers = value
        return self

    def get_result(self):
        """ Gets a built pizza"""
        return self._pizza
