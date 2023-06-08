#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]
    operators = ['+', '-', '*', '/']
    func = [add, sub, mul, div]

    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    for i in range(4):
        if operator == operators[i]:
            print("{} {} {} = {}".format(a, operator, b, func[i](a, b)))
