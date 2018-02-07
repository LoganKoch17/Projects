from turtle import Turtle

def square(t: Turtle, length: int) -> None:
    """
    Draw a square with a given length
    :param t: an instance of a Turtle used
    :param length: Length of the side of the shape
    :return: None
    """
    for count in range(4):
        t.forward(length)
        t.left(90)

#def regular_polygon(t: Turtle, length: int, num_sides = 4)

def hexagon(t: Turtle, length: int) -> None:
    """
    Draw a hexagon with a given length
    :param t: an instance of a Turtle used
    :param length: Length of the side of the shape
    :return: None
    """

    for count in range(6):
        t.forward(length)
        t.left(60)


def triangle(t: Turtle, length: int) -> None:
    """
    Draw a triangle with a given length
    :param t: an instance of a Turtle used
    :param length: Length of the side of the shape
    :return: None
    """

    for count in range(6):
        t.forward(length)
        t.left(120)


def octagon(t: Turtle, length: int) -> None:
    """
    Draw a octagon with a given length
    :param t: an instance of the Turtle used
    :param length: Length of the side of the shape
    :return: None
    """

    for count in range(6):
        t.forward(length)
        t.left(45)

def main() -> int:
    yertle = Turtle
    square(yertle, 300)

if __name__ == '__main__':
    main()