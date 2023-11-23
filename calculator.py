def calculator():
    check = False
    num1 = 0
    num2 = 0
    while not check:
        try:
            num1 = float(input("Num1: "))
            num2 = float(input("Num2: "))
            check = True
        except ValueError:
            print("Input 2 nums!")

    check = False
    oper = ""
    while not check:
        oper = input("Input operation(add,sub,mul,div): ")
        if oper in ("add", "sub", "mul", "div"):
            check = True

    match oper:
        case "add":
            print(__add(num1, num2))
        case "sub":
            print(__sub(num1, num2))
        case "mul":
            print(__mul(num1, num2))
        case "div":
            print(__div(num1, num2))


def __add(num1, num2):
    return num1 + num2


def __sub(num1, num2):
    return num1 - num2


def __mul(num1, num2):
    return num1 * num2


def __div(num1, num2):
    if num2 == 0:
        return 0
    return num1 / num2


if __name__ == '__main__':
    calculator()
