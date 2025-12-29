
import numpy as np

class NumpyCreator:
    def from_list(self, lst, dtype = None):
        return np.array(lst, dtype)
    def from_tuple(self, tpl, dtype = None):
        return np.array(tpl, dtype)
    def from_iterable(self, itr, dtype = None):
        return np.fromiter(itr, dtype)
    def from_shape(self, shape, value = 0, dtype = None):
        return np.full(shape, value, dtype)
    def random(self, shape):
        return np.random.random(shape)
    def identity(self, n, dtype = None):
        return np.eye(n, dtype)
    

# Write a class named NumPyCreator, that implements all of the following methods.
# Each method receives as an argument a different type of data structure and transforms
# it into a Numpy array:
# • from_list(self, lst): takes a list or nested lists and returns its corresponding
# Numpy array.
# • from_tuple(self, tpl): takes a tuple or nested tuples and returns its correspond-
# ing Numpy array.
# • from_iterable(self, itr): takes an iterable and returns an array which contains
# all of its elements.
# • from_shape(self, shape, value): returns an array filled with the same value.
# The first argument is a tuple which specifies the shape of the array, and the second
# argument specifies the value of the elements. This value must be 0 by default.
# • random(self, shape): returns an array filled with random values. It takes as an
# argument a tuple which specifies the shape of the array.
# 3
# Python & ML - Module 03 Numpy
# • identity(self, n): returns an array representing the identity matrix of size n.
# BONUS: Add to these methods an optional argument which specifies the datatype
# (dtype) of the array (e.g. to represent its elements as integers, floats, ...)


npc = NumpyCreator()
print(npc.from_list([[1,2,3],[6,3,4]]))
# # Output :
# # array([[1, 2, 3],
# #     [6, 3, 4]])
# print(npc.from_list([[1,2,3],[6,4]]))
# # Output :
# # None
print(npc.from_list([[1,2,3],['a','b','c'],[6,4,7]]))
# # Output :
# # array([['1','2','3'],
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