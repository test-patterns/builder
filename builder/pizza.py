""" Sample problem featuring the builder pattern. """

class Pizza(object):
    """ A pizza """

    def __init__(self):
        """ Initializes a new pizza """
        self.crust = None
        self.cheese = None
        self.pepperoni = None
        self.mushrooms = None
        self.onions = None
        self.sausage = None
        self.bacon = None
        self.peppers = None

    def __str__(self):
        """ Gets a string representation of a pizza """
        pizza = "This is a " + self.crust + " pizza with "

        if (self.cheese != None):
            pizza += self.cheese + " Cheese, "
        if (self.pepperoni != None):
            pizza += self.pepperoni + " Pepperoni, "
        if (self.mushrooms != None):
            pizza += self.mushrooms + " Mushrooms, "
        if (self.onions != None):
            pizza += self.onions + " Onions, "
        if (self.sausage != None):
            pizza += self.sausage + " Sausage, "
        if (self.bacon != None):
            pizza += self.bacon + " Bacon, "
        if (self.peppers != None):
            pizza += self.peppers + " Peppers, "

        if (pizza[-2:] == ", "):
            return pizza[:-2]
        else:
            return pizza[:-6]
