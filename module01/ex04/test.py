
"""
Test script for the Vector class.
"""

from vector import Vector


def test_multiplication():
    """Test vector multiplication by scalar."""
    print("------------1st tests -----------")
    # Column vector of shape n * 1
    v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
    v2 = v1 * 5
    print(v2)
    # Expected: Vector([[0.0], [5.0], [10.0], [15.0]])

    # Row vector of shape 1 * n
    v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
    v2 = v1 * 5
    print(v2)
    # Expected: Vector([[0.0, 5.0, 10.0, 15.0]])

    v2 = v1 / 2.0
    print(v2)
    # Expected: Vector([[0.0, 0.5, 1.0, 1.5]])

    # v1 / 0.0 would raise ZeroDivisionError
    # 2.0 / v1 would raise NotImplementedError


def test_shape_and_values():
    """Test shape and values attributes."""
    print("------------2nd tests -----------")
    # Column vector
    v = Vector([[0.0], [1.0], [2.0], [3.0]])
    print(v.shape)  # Expected: (4, 1)
    print(v.values)  # Expected: [[0.0], [1.0], [2.0], [3.0]]

    # Row vector
    v = Vector([[0.0, 1.0, 2.0, 3.0]])
    print(v.shape)  # Expected: (1, 4)
    print(v.values)  # Expected: [[0.0, 1.0, 2.0, 3.0]]


def test_transpose():
    """Test transpose operation."""
    print("------------3rd tests -----------")
    v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
    print(v1.shape)  # Expected: (4, 1)
    print(v1.T())    # Expected: transposed vector


if __name__ == "__main__":
    test_multiplication()
    test_shape_and_values()
    test_transpose()
# Expected output:
# Vector([[0.0, 1.0, 2.0, 3.0]])
print(v1.T().shape)
# Expected output:
# (1,4)
# Example 2:
v2 = Vector([[0.0, 1.0, 2.0, 3.0]])
print(v2.shape)
# Expected output:
# (1,4)
print(v2.T())
# Expected output:
# Vector([[0.0], [1.0], [2.0], [3.0]])
print(v2.T().shape)
# Expected output:
# (4,1)

print("------------4st tests -----------")
# Example 1:
v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
v2 = Vector([[2.0], [1.5], [2.25], [4.0]])
print(v1.dot(v2))
# Expected output:
# 18.0
v3 = Vector([[1.0, 3.0]])
v4 = Vector([[2.0, 4.0]])
print(v3.dot(v4))
# Expected output:
# 13.0
v1
# Expected output: to see what __repr__() should do
# [[0.0, 1.0, 2.0, 3.0]]
print(v1)
# Expected output: to see what __str__() should do
# [[0.0, 1.0, 2.0, 3.0]]

