#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]
    flag = 0
    operators = ['+', '-', '*', '/']
    func = [add, sub, mul, div]

    for op in operators:
        if op == operator:
            flag = 1
            break
    if flag == 0:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    for i in range(4):
        if operator == operators[i]:
            print("{} {} {} = {}".format(a, b, operator, func[i](a, b)))
