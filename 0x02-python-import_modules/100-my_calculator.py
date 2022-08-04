#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    from calculation_1 import add, sub, mul, div

    n = len(argv)
    if n != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif argv[2] not in ("+", "-", "*", "/"):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])

        if argv[2] == "+":
            print("{} {} {} = {}".format(a, argv[2], b, add(a, b)))
        if argv[2] == "-":
            print("{} {} {} = {}".format(a, argv[2], b, sub(a, b)))
        if argv[2] == "*":
            print("{} {} {} = {}".format(a, argv[2], b, mul(a, b)))
        if argv[2] == "+":
            print("{} {} {} = {}".format(a, argv[2], b, div(a, b)))




