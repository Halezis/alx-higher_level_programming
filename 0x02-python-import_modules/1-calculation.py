#!/usr/bin/python3

import calculator_1 as calculator
a = 10
b = 5

if __name__ == "__main__":
    print("{} + {} = {}".format(a, b, calculator.add(a, b)))
    print("{} - {} = {}".format(a, b, calculator.sub(a, b)))
    print("{} * {} = {}".format(a, b, calculator.mul(a, b)))
    print("{} / {} = {}".format(a, b, calculator.div(a, b)))
