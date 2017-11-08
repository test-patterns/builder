# Builder Pattern
Sample problem featuring the builder pattern.

Use the builder pattern to create an object from a bunch of other objects.

## Task 1 - Add a build property

Welcome to Pizza<sup>2</sup>! Our kitchen already adds ingredients to pizzas, but we don't have olives on the menu yet. See for yourself by running the following command:

```
python builder -c Thin -x Mozzarella -p Uncured -e Green
```

Add the new ingredient, olives, to the pizza builder.

### UML

![alt text](http://yuml.me/61ef4b7b.png)
[edit](http://yuml.me/edit/61ef4b7b)

### Previous output

```
This is a Thin pizza with Mozzarella Cheese, Uncured Pepperoni, Green Peppers
```

### Desired output

```
example:
This is a Thin pizza with Mozzarella Cheese, Uncured Pepperoni, Green Peppers, Black Olives
```

## Task 2 - Testing

Our test coverage is pretty terrible. See for yourself by running the following commands:

```
coverage run --source builder -m unittest discover tests
coverage report -m
```

Increase this to 100%.
