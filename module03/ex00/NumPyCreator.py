
"""
NumPy array creation utilities.
"""

import numpy as np
from typing import Union, Tuple, Any, Optional


class NumpyCreator:
    """A class to create NumPy arrays from various data structures."""

    @staticmethod
    def from_list(lst: list, dtype: Optional[str] = None) -> np.ndarray:
        """
        Create a NumPy array from a list or nested lists.

        Args:
            lst: A list or nested lists.
            dtype: Optional data type for the array.

        Returns:
            NumPy array.
        """
        return np.array(lst, dtype=dtype)

    @staticmethod
    def from_tuple(tpl: tuple, dtype: Optional[str] = None) -> np.ndarray:
        """
        Create a NumPy array from a tuple or nested tuples.

        Args:
            tpl: A tuple or nested tuples.
            dtype: Optional data type for the array.

        Returns:
            NumPy array.
        """
        return np.array(tpl, dtype=dtype)

    @staticmethod
    def from_iterable(itr: Any, dtype: Optional[str] = None) -> np.ndarray:
        """
        Create a NumPy array from an iterable.

        Args:
            itr: An iterable object.
            dtype: Optional data type for the array.

        Returns:
            NumPy array.
        """
        return np.fromiter(itr, dtype=dtype)

    @staticmethod
    def from_shape(shape: Tuple[int, ...], value: Union[int, float] = 0, dtype: Optional[str] = None) -> np.ndarray:
        """
        Create a NumPy array filled with a specific value.

        Args:
            shape: Tuple specifying the array shape.
            value: Value to fill the array with (default: 0).
            dtype: Optional data type for the array.

        Returns:
            NumPy array filled with value.
        """
        return np.full(shape, value, dtype=dtype)

    @staticmethod
    def random(shape: Tuple[int, ...]) -> np.ndarray:
        """
        Create a NumPy array filled with random values.

        Args:
            shape: Tuple specifying the array shape.

        Returns:
            NumPy array with random values [0, 1).
        """
        return np.random.random(shape)

    @staticmethod
    def identity(n: int, dtype: Optional[str] = None) -> np.ndarray:
        """
        Create an identity matrix of size n×n.

        Args:
            n: Size of the matrix.
            dtype: Optional data type for the array.

        Returns:
            Identity matrix as NumPy array.
        """
        return np.eye(n, dtype=dtype)


if __name__ == "__main__":
    npc = NumpyCreator()
    print(npc.from_list([[1, 2, 3], [6, 3, 4]]))
    print(npc.from_list([[1, 2, 3], ['a', 'b', 'c'], [6, 4, 7]]))
    print(npc.from_tuple((1, 2, 3)))
    print(npc.from_iterable(range(5)))
    print(npc.from_shape((2, 3), 42))
    print(npc.identity(3))
# # ['a','b','c'],
# # ['6','4','7'], dtype='<U21'])
print( npc.from_list(((1,2),(3,4))))
# # Output :
# # None
print(npc.from_tuple(("a", "b", "c")))
# # Output :
# # array(['a', 'b', 'c'])
print(npc.from_tuple(["a", "b", "c"]))
# # Output :
# # None
print(npc.from_iterable(range(5)))
# # Output :
# # array([0, 1, 2, 3, 4])
shape=(3,5)
print(npc.from_shape(shape))
# # Output :
# # array([[0, 0, 0, 0, 0],
# # [0, 0, 0, 0, 0],
# # [0, 0, 0, 0, 0]])
print(npc.random(shape))
# # Output :
# # array([[0.57055863, 0.23519999, 0.56209311, 0.79231567, 0.213768 ],
# # [0.39608366, 0.18632147, 0.80054602, 0.44905766, 0.81313615],
# # [0.79585328, 0.00660962, 0.92910958, 0.9905421 , 0.05244791]])
print(npc.identity(4))
# # Output :
# # array([[1., 0., 0., 0.],
# # [0., 1., 0., 0.],
# # [0., 0., 1., 0.],
# # [0., 0., 0., 1.]])