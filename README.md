# Builder Pattern
Sample problem featuring the builder pattern.

## Task 1 - Add a build property

Welcome to Pizza<sup>2</sup>! Our kitchen already adds ingredients to pizzas, but we don't have olives on the menu yet. See for yourself by running the following command:

```
python builder -c Thin -x Mozzarella -p Uncured -e Green
```

Add the new ingredient, olives, to the pizza builder.

## Task 2 - Testing

Our test coverage is pretty terrible. See for yourself by running the following commands:

```
coverage run --source builder -m unittest discover tests
coverage report -m
```

Increase this to 100%.
