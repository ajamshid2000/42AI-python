
"""
Vector class for 1D vector operations.
"""

from typing import List, Union, Tuple
import copy


class Vector:
    """
    A class representing a 1D vector.

    Attributes:
        values: The vector values as a list of lists.
        shape: Tuple (rows, cols) where one is 1.
    """

    def __init__(self, values: Union[int, List[List[float]]], upper: Union[int, float, None] = None) -> None:
        """
        Initialize a Vector.

        Args:
            values: If int, creates range(0, values). If list of lists, the vector values.
            upper: If values is int, creates range(values, upper).

        Raises:
            TypeError: If invalid types.
            ValueError: If invalid range.
        """
        if isinstance(values, int) and upper is None:
            self.values = [[float(i)] for i in range(values)]
        elif isinstance(values, int) and upper is not None:
            if not isinstance(upper, (int, float)):
                raise TypeError("Upper value must be a number")
            if upper < values:
                raise ValueError("Invalid range: start cannot be greater than end")
            self.values = [[float(i)] for i in range(values, int(upper))]
        elif isinstance(values, list):
            self.values = copy.deepcopy(values)
        else:
            raise TypeError("Values must be int or list of lists")

        # Validate and set shape
        if len(self.values) > 1:
            # Column vector
            for row in self.values:
                if len(row) != 1 or not isinstance(row[0], (int, float)):
                    raise TypeError("Invalid vector format")
            self.shape = (len(self.values), 1)
        else:
            # Row vector
            for val in self.values[0]:
                if not isinstance(val, (int, float)):
                    raise TypeError("Invalid vector format")
            self.shape = (1, len(self.values[0]))

    def __str__(self) -> str:
        """Return string representation."""
        return str(self.values)

    def __repr__(self) -> str:
        """Return repr representation."""
        return f"Vector({self.values})"

    def __add__(self, other: 'Vector') -> 'Vector':
        """Add two vectors."""
        if self.shape != other.shape:
            raise ValueError("Vectors must have the same shape")
        if self.shape[0] > 1:
            new_values = [[a[0] + b[0]] for a, b in zip(self.values, other.values)]
        else:
            new_values = [[a + b for a, b in zip(self.values[0], other.values[0])]]
        return Vector(new_values)

    def __radd__(self, other: 'Vector') -> 'Vector':
        """Reverse add."""
        return self + other

    def __sub__(self, other: 'Vector') -> 'Vector':
        """Subtract two vectors."""
        if self.shape != other.shape:
            raise ValueError("Vectors must have the same shape")
        if self.shape[0] > 1:
            new_values = [[a[0] - b[0]] for a, b in zip(self.values, other.values)]
        else:
            new_values = [[a - b for a, b in zip(self.values[0], other.values[0])]]
        return Vector(new_values)

    def __rsub__(self, other: 'Vector') -> 'Vector':
        """Reverse subtract."""
        return (-1 * self) + other

    def __mul__(self, scalar: Union[int, float]) -> 'Vector':
        """Multiply by scalar."""
        if not isinstance(scalar, (int, float)):
            raise TypeError("Scalar must be a number")
        if self.shape[0] > 1:
            new_values = [[val[0] * scalar] for val in self.values]
        else:
            new_values = [[val * scalar for val in self.values[0]]]
        return Vector(new_values)

    def __rmul__(self, scalar: Union[int, float]) -> 'Vector':
        """Reverse multiply."""
        return self * scalar

    def __truediv__(self, scalar: Union[int, float]) -> 'Vector':
        """Divide by scalar."""
        if not isinstance(scalar, (int, float)):
            raise TypeError("Scalar must be a number")
        if scalar == 0:
            raise ZeroDivisionError("Division by zero")
        return self * (1 / scalar)

    def __rtruediv__(self, other):
        """Reverse division not implemented."""
        raise NotImplementedError("Division of scalar by Vector not defined")

    def dot(self, other: 'Vector') -> float:
        """
        Compute dot product.

        Args:
            other: Another Vector.

        Returns:
            Dot product as float.
        """
        if self.shape != other.shape:
            raise ValueError("Vectors must have the same shape")
        result = 0.0
        if self.shape[0] > 1:
            for a, b in zip(self.values, other.values):
                result += a[0] * b[0]
        else:
            for a, b in zip(self.values[0], other.values[0]):
                result += a * b
        return result

    def T(self) -> 'Vector':
        """Transpose the vector."""
        if self.shape[0] > 1:
            new_values = [[self.values[i][0] for i in range(self.shape[0])]]
        else:
            new_values = [[self.values[0][i]] for i in range(self.shape[1])]
        return Vector(new_values)
        
        

                


        
# v1 = Vector(3, 6)
# print(v1)
# print(v1.shape)
# # v2 = Vector([[2],[2],[2]])
# # v3 = v1 + v2
# # print(v3)
# # v3 = 5 * v1
# # print(v3)