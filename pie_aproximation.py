import math
from random import random


def pie_aprox():

    radius = 10
    check = False
    num_dots = 0

    while not check:
        try:
            num_dots = int(input("Input number of dots: "))
            check = True
        except ValueError:
            print("You must enter integer!")

    inside = 0
    for i in range(num_dots):
        x = random() * 2 * radius - radius
        y = random() * 2 * radius - radius
        distance = math.sqrt(x * x + y * y)
        if distance < radius:
            inside = inside + 1

    pie = inside / num_dots * 4
    print("Pie = ", pie)


if __name__ == '__main__':
    pie_aprox()
