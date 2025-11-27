
class Vector:
    def __init__(self, lower_or_list, upper = None):
        if(isinstance(lower_or_list, int) and upper == None):
            self.values = ([[float(x)] for x in range(lower_or_list)])
        elif(upper != None):
            if(not isinstance(upper, (int, float))):
                raise TypeError("upper value not an int")
            if(upper < lower_or_list):
                raise ValueError("Invalid range: start value cannot be greater than end value.")
            self.values = ([[float(x)] for x in range(lower_or_list, upper)])
        elif(not isinstance(lower_or_list, list)):
            raise TypeError("parameter not an int or list")
        else: self.values = lower_or_list
        if(len(self.values) > 1):
            for x in self.values:
                if(len(x) > 1):
                    raise TypeError("multiple columns and rows make a matrix")
                if not(isinstance(x[0], (int, float))):
                    raise ArithmeticError("arithmatic operation on invalid type in a column")
            self.shape = (len(self.values), 1)
        else: 
            for x in self.values[0]:
                if not(isinstance(x, (int, float))):
                    raise ArithmeticError("arithmatic operation on invalid type in a row")
            self.shape = (1, len(self.values[0]))
   
    def __str__(self):
        return str(self.values)
    
    def __repr__(self):
        return f'{self.values}'

    def __add__(self, other):
        if (self.shape != other.shape):
            raise TypeError("shapes of the passed ojects are not same")
        if (len(self.values) > 1):
           return Vector([[x[0] + y[0]] for x, y in zip(self.values, other.values)])
        else:
            return Vector([[x + y for x, y in zip(self.values[0], other.values[0])]])
    def __radd__(self, other):
        self.__add__(other)

    def __sub__(self, other):
        if (self.shape != other.shape):
            raise TypeError("shapes of the passed ojects are not same")
        if (len(self.values) > 1):
           return Vector([[x[0] - y[0]] for x, y in zip(self.values, other.values)])
        else:
            return Vector([[x - y for x, y in zip(self.values[0], other.values[0])]])
    def __rsub__(self, other):
        self.__sub__(other)

    def __rmul__(self, other):
        if not (isinstance(other, (int, float))):
            raise ArithmeticError("operation on non number caught")
        if (len(self.values) > 1):
           return Vector([[x[0] * other] for x in self.values])
        else:
            return Vector([[x * other for x in self.values[0]]])

    def __mul__(self, other):
        return self.__rmul__(other)
    
    def __truediv__(self, other):
        if not (isinstance(other, (int, float))):
            raise ArithmeticError("operation on non number caught")
        if(other == 0):
            raise ZeroDivisionError("division by zero.")
        if (len(self.values) > 1):
           return Vector([[x[0] / other] for x in self.values])
        else:
            return Vector([[x / other for x in self.values[0]]])
    def __rtruediv__(self, other):
        raise NotImplementedError("Division of a scalar by a Vector is not defined here")

    def dot(self, vector):
        res = 0.0
        if(len(vector.values) > 1):
            for x in vector.values:
                if(len(x) > 1):
                    raise TypeError("multiple columns and rows make a matrix")
                if not(isinstance(x[0], (int, float))):
                    raise ArithmeticError("arithmatic operation on invalid type in a column")
            for x in range(len(vector.values)):
                res += self.values[x][0] * vector.values[x][0]
        else: 
            for x in vector.values[0]:
                if not(isinstance(x, (int, float))):
                    raise ArithmeticError("arithmatic operation on invalid type in a row")
            for x in range(len(vector.values[0])):
                res += self.values[0][x] * vector.values[0][x]
        return res
    def T(self):
        if (len(self.values) > 1):
            new_obj = Vector([[self.values[x][0] for x in range(self.shape[0])]])
        else:
            new_obj = Vector([[self.values[0][x]] for x in range(self.shape[1])])
        return new_obj
        
        

                


        
# v1 = Vector(3, 6)
# print(v1)
# print(v1.shape)
# # v2 = Vector([[2],[2],[2]])
# # v3 = v1 + v2
# # print(v3)
# # v3 = 5 * v1
# # print(v3)