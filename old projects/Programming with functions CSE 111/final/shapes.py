import math
import sys
pi = math.pi

volume = 0

def get_shapes_input(shape=None):
    """
    Prompts the user for a shape and validates the input.

    Args:
        shape (str): Optional shape name. If provided, the function directly checks its validity.

    Returns:
        str: Valid shape name if input is valid, otherwise None.
    """
    if "pytest" in sys.modules:
        if shape is None:
            shape = input("What shape would you like? ")

        shape = shape.lower().replace(" ", "_")

        if shape in {"sphere", "torus", "cylinder", "cone", "cube", "cuboid", "rectangular_prism", "triangular_prism", "square_pyramid", "triangular_pyramid" }:
            return shape
        else:
            print("That was not a shape we are able to find the volume of. Please check your spelling.")
            return None
    else:
        shape = input("What shape would you like? ")
        shape = shape.lower().replace(" ", "_")

        if shape in {"sphere", "torus", "cylinder", "cone", "cube", "cuboid", "rectangular_prism", "triangular_prism", "square_pyramid", "triangular_pyramid"}:
            return shape
        elif shape == "help":
            print("the shapes availiable are sphere, torus, cylinder, cone, cube, cuboid, rectangular prism, triangular prism, square pyramid, pyramid, or triangular pyramid")
            return None
        else:
            print("That was not a shape we are able to find the volume of. Please check your spelling, or enter \"help\" for a full list of shapes")
            return None


def get_rounding_input(rounding = 0):
    """
    Prompts the user for the number of decimal places to round to and validates the input.

    Args:
        rounding (int): Optional rounding value. If provided, the function directly checks its validity.

    Returns:
        int or str: Valid rounding value if input is valid, otherwise a string indicating the error message.
    """
    while True:
        if "pytest" in sys.modules:

            try:
                int(rounding)
            except:
                print("please enter an integer")
            if rounding >0:
                return rounding
            else:
                return "please enter a positive integer"
        else:
            try:
                rounding = int(input("to how many decimal places would you like to round?"))
            except:
                print("please enter an integer")
            if rounding >0:
                return rounding
            else:
                print("please enter a positive integer")
            continue

            

# Functions to calculate the volume of various shapes

def sphere(r):
    """
    Calculates the volume of a sphere.

    Args:
        r (float): Radius of the sphere.

    Returns:
        float: Volume of the sphere.
    """
    volume = (4 / 3) * pi * r ** 3
    return volume


def torus(r, R):
    """
    Calculates the volume of a torus.

    Args:
        r (float): Minor radius of the torus.
        R (float): Major radius of the torus.

    Returns:
        float: Volume of the torus.
    """
    volume = (pi * r ** 2) * (2 * pi * R)
    return volume


def cylinder(r, h):
    """
    Calculates the volume of a cylinder.

    Args:
        r (float): Radius of the cylinder.
        h (float): Height of the cylinder.

    Returns:
        float: Volume of the cylinder.
    """
    volume = pi * r ** 2 * h
    return volume


def cone(r, h):
    """
    Calculates the volume of a cone.

    Args:
        r (float): Radius of the cone.
        h (float): Height of the cone.

    Returns:
        float: Volume of the cone.
    """
    volume = (1/3) * pi * (r ** 2) * h 
    return volume


def cube(side):
    """
    Calculates the volume of a cube.

    Args:
        side (float): Length of the side of the cube.

    Returns:
        float: Volume of the cube.
    """
    volume = side ** 3
    return volume


def cuboid(length, width, height):
    """
    Calculates the volume of a cuboid.

    Args:
        length (float): Length of the cuboid.
        width (float): Width of the cuboid.
        height (float): Height of the cuboid.

    Returns:
        float: Volume of the cuboid.
    """
    volume = length * width * height
    return volume


def triangular_pyramid(base, base_height, height):
    """
    Calculates the volume of a triangular pyramid.

    Args:
        base (float): Length of one side of the base triangle.
        base_height (float): Height of the base triangle.
        height (float): Height of the triangular pyramid.

    Returns:
        float: Volume of the triangular pyramid.
    """
    base_triangle = (1/2) * base * base_height
    volume = (1/3) * base_triangle * height
    return volume


def square_pyramid(base, height):
    """
    Calculates the volume of a square pyramid.

    Args:
        base (float): Base length of the square pyramid.
        height (float): Height of the square pyramid.

    Returns:
        float: Volume of the square pyramid.
    """
    volume = (base ** 2) * (height / 3)
    return volume


def triangular_prism(base, height, length):
    """
    Calculates the volume of a triangular prism.

    Args:
        base (float): Base length of the triangular prism.
        height (float): Height of the triangular prism.
        length (float): Length of the triangular prism.

    Returns:
        float: Volume of the triangular prism.
    """
    base_area = (1/2) * base * height
    volume = base_area * length
    return volume

def main():
    """
    Entry point of the program.
    Prompts the user for shape and rounding input, and calculates the volume accordingly.
    """
    shape = get_shapes_input("")
    if shape != None:
        rounding = get_rounding_input()

    # Calculate the volume based on the selected shape
    if shape == "sphere":
        r = float(input("What is the radius of your sphere? "))
        volume = sphere(r)
    elif shape == "torus":
        r = float(input("What is the minor radius of your torus? "))
        R = float(input("What is the major radius of your torus? "))
        volume = torus(r, R)
    elif shape == "cylinder":
        r = float(input("What is the radius of your cylinder? "))
        h = float(input("What is the height of your cylinder? "))
        volume = cylinder(r, h)
    elif shape == "cone":
        r = float(input("What is the radius of your cone? "))
        h = float(input("What is the height of your cone? "))
        volume = cone(r, h)
    elif shape == "cube":
        side = float(input("What is the length of the side of your cube? "))
        volume = cube(side)
    elif shape == "cuboid" or shape == "rectangular_prism":
        length = float(input("What is the length of your cuboid? "))
        width = float(input("What is the width of your cuboid? "))
        height = float(input("What is the height of your cuboid? "))
        volume = cuboid(length, width, height)
    elif shape == "triangular_pyramid":
        base = float(input("What is the length of one side of your base triangle? "))
        base_height = float(input("What is the height of your base triangle? "))
        height = float(input("What is the height of your triangular pyramid? "))
        volume = triangular_pyramid(base, base_height, height)
    elif shape == "square_pyramid" or shape == "pyramid":
        base = float(input("What is the base length of your square pyramid? "))
        height = float(input("What is the height of your square pyramid? "))
        volume = square_pyramid(base, height)
    elif shape == "triangular_prism":
        base = float(input("What is the base length of your triangular prism? "))
        height = float(input("What is the height of your triangular prism? "))
        length = float(input("What is the length of your triangular prism? "))
        volume = triangular_prism(base, height, length)
    elif shape == None:
        # If no shape is selected, restart the program
        main()

    # Print the calculated volume with the desired rounding
    print(f"The volume of your shape is {volume:.{rounding}f}")


if __name__ == "__main__":
    main()