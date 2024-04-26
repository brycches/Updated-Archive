import pytest
from shapes import (
    sphere,
    torus,
    cylinder,
    cone,
    cube,
    cuboid,
    triangular_pyramid,
    square_pyramid,
    triangular_prism,
    get_shapes_input,
    get_rounding_input,
)
import sys
import io
# Test sphere()
def test_sphere():
    assert sphere(2) == 33.510321638291124
    assert sphere(5) == 523.5987755982989
    assert sphere(10) == 4188.790204786391


# Test torus()
def test_torus():
    assert torus(2, 4) == 315.82734083485946
    assert torus(3, 6) == 1065.9172753176506
    assert torus(5, 8) == 3947.8417604357433


# Test cylinder()
def test_cylinder():
    assert cylinder(2, 4) == 50.26548245743669
    assert cylinder(3, 6) == 169.64600329384882
    assert cylinder(5, 8) == 628.3185307179587


# Test cone()
def test_cone():
    assert cone(2, 4) == 16.755160819145562
    assert cone(3, 6) == 56.548667764616276
    assert cone(5, 8) == 209.43951023931953


# Test cube()
def test_cube():
    assert cube(2) == 8.0
    assert cube(3) == 27.0
    assert cube(5) == 125.0


# Test cuboid()
def test_cuboid():
    assert cuboid(2, 4, 6) == 48.0
    assert cuboid(3, 5, 8) == 120.0
    assert cuboid(4, 6, 10) == 240.0


# Test triangular_pyramid()
def test_triangular_pyramid():
    assert triangular_pyramid(4, 6, 6) == 24.0
    assert triangular_pyramid(5, 8, 8) == 53.33333333333333
    assert triangular_pyramid(10, 12, 12) == 240.0


# Test square_pyramid()
def test_square_pyramid():
    assert square_pyramid(4, 6) == 32.0
    assert square_pyramid(5, 8) == 66.66666666666666
    assert square_pyramid(10, 12) == 400.0


# Test triangular_prism()
def test_triangular_prism():
    assert triangular_prism(4, 6, 8) == 96.0
    assert triangular_prism(5, 8, 10) == 200.0
    assert triangular_prism(10, 12, 15) == 900.0


def test_get_shapes_input():
    inputs = ["sphere", "torus", "cylinder", "cone", "cube", "cuboid", "rectangular_prism"]
    expected_outputs = ["sphere", "torus", "cylinder", "cone", "cube", "cuboid", "rectangular_prism"]

    for i in range(len(inputs)):
        shape = inputs[i]
        expected_output = expected_outputs[i]

        assert get_shapes_input(shape) == expected_output


# Test get_rounding_input()
def test_get_rounding_input(capsys):
    inputs = [2, 5, -3, 0, 4]
    expected_outputs = [2, 5, "please enter a positive integer", "please enter a positive integer", 4]

    for i in range(len(inputs)):
        rounding = inputs[i]
        expected_output = expected_outputs[i]

        rounding_input = get_rounding_input(rounding)
        captured_out, _ = capsys.readouterr()

        assert rounding_input == expected_output



# Run all the tests
if __name__ == "__main__":
    pytest.main()