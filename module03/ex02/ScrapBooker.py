
import numpy as np
class ScrapBooker:
    def crop(self, array, dim, position=(0,0)):
        """
        Crops the image as a rectangle via dim arguments (being the new height
        and width of the image) from the coordinates given by position arguments.
        Args:
        -----
        array: numpy.ndarray
        dim: tuple of 2 integers.
        position: tuple of 2 integers.
        Returns:
        -------
        new_arr: the cropped numpy.ndarray.
        None: (if the combination of parameters is not possible).
        Raises:
        ------
        This function should not raise any Exception.
        """
        if dim[0] + position[0] > array.shape[0] or dim[1] + position[1] > array.shape[1] or not isinstance(array, np.ndarray):
            return None
        return array[position[0]:position[0]+dim[0], position[1]:position[1]+dim[1]]
    
    def thin(self, array, n, axis):
        """
        Deletes every n-th line pixels along the specified axis (0: vertical, 1: horizontal)
        Args:
        -----
        array: numpy.ndarray.
        n: non null positive integer lower than the number of row/column of the array
        (depending of axis value).
        axis: positive non null integer.
        Returns:
        -------
        new_arr: thined numpy.ndarray.
        None: (if the combination of parameters is not possible).
        Raises:
        ------
        This function should not raise any Exception.
        """
        if(axis > 2 or not isinstance(array, np.ndarray)):
            return None
        ax = 1 if(axis == 0) else 0
        print(np.arange(n-1, array.shape[axis], n))
        return np.delete(array, np.arange(n-1, array.shape[ax], n), ax)
    def juxtapose(self, array, n, axis):
        """
        Juxtaposes n copies of the image along the specified axis.
        Args:
        -----
        array: numpy.ndarray.
        n: positive non null integer.
        axis: integer of value 0 or 1.
        Returns:
        -------
        new_arr: juxtaposed numpy.ndarray.
        None: (if the combination of parameters is not possible).
        Raises:
        -------
        This function should not raise any Exception.
        """
        if(axis > 2 or not isinstance(array, np.ndarray) or not n > 0):
            return None
        return np.tile(array, (1 if axis == 1 else n, n if axis == 1 else 1))

    def mosaic(self, array, dim):
        """
        Makes a grid with multiple copies of the array. The dim argument specifies
        the number of repetition along each dimensions.
        Args:
        -----
        array: numpy.ndarray.
        dim: tuple of 2 integers.
        Return:
        -------
        new_arr: mosaic numpy.ndarray.
        None (combinaison of parameters not compatible).
        Raises:
        -------
        This function should not raise any Exception.
        """
        if(not isinstance(dim, tuple) or len(dim) > 2 or not isinstance(array, np.ndarray)):
            return None
        return np.tile(array, (dim[1],dim[0]))

spb = ScrapBooker()
arr1 = np.arange(0,25).reshape(5,5)
print(spb.crop(arr1, (3,1),(1,0)))

arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1,9)
# print(arr2)
print(spb.thin(arr2,3,0))

arr3 = np.array([[1, 2, 3],[1, 2, 3],[1, 2, 3]])
print(spb.juxtapose(arr3, 3, 1))