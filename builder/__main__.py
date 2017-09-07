#!/usr/bin/env python
""" Sample problem featuring the builder pattern. """

import argparse

from pizza_builder import PizzaBuilder

def main():
    """ Execute the program """
    args = parse_args()
    pizza = PizzaBuilder() \
        .set_crust(args.crust) \
        .set_cheese(args.cheese) \
        .set_pepperoni(args.pepperoni) \
        .set_mushrooms(args.mushrooms) \
        .set_onions(args.onions) \
        .set_sausage(args.sausage) \
        .set_bacon(args.bacon) \
        .set_peppers(args.peppers) \
        .get_result()
        # .set_olives("Olives") \
    print(pizza)

def parse_args():
    """ Parse input arguments """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c",
        "--crust",
        help="The type of crust to order.",
        required=True)
    parser.add_argument(
        "-x",
        "--cheese",
        help="The type of cheese to order.",
        required=False)
    parser.add_argument(
        "-p",
        "--pepperoni",
        help="The type of pepperoni to order.",
        required=False)
    parser.add_argument(
        "-m",
        "--mushrooms",
        help="The type of mushrooms to order.",
        required=False)
    parser.add_argument(
        "-o",
        "--onions",
        help="The type of onions to order.",
        required=False)
    parser.add_argument(
        "-s",
        "--sausage",
        help="The type of sausage to order.",
        required=False)
    parser.add_argument(
        "-b",
        "--bacon",
        help="The type of bacon to order.",
        required=False)
    parser.add_argument(
        "-e",
        "--peppers",
        help="The type of peppers to order.",
        required=False)
    return parser.parse_args()

if __name__ == "__main__":
    main()
