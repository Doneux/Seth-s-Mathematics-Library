#Seth's Vector Classes
#2d and 3d

#Vectors handle vector components only. Norm and angle need separate implementation.

import math

class Vector3d:
    def __init__(self, i=0, j=0, k=0):
        self.dim = 3
        self.i = i
        self.j = j
        self.k = k
    
    def __add__(self, u1):
        return Vector2d(self.i + u1.i, self.j + u1.j, self.k + u1.k)
    
    def __sub__(self, u1):
        return Vector2d(self.i - u1.i, self.j - u1.j, self.k - u1.k)
    
    def __mul__(self, c1):
        ##Scalar multiplication. For cross and dot, see cross and dot.
        return Vector2d(self.i * c1, self.j * c1, self.k * c1)
    
    def __neg__(self):
        return Vector2d(-self.i, -self.j, -self.k)
    
    def __div__(self, c1):
        #I really don't like scalar division. Please just multiply by a fractional scalar.
        if c1 != 0:
            return Vector2d(self.i / c1, self.j / c1, self.k / c1)
        else:
            return None
        
    def norm(self):
        return math.sqrt((self.i * self.i) + (self. j * self.j) + (self.k * self.k))

    def dot(self, u1):
        return ((self.i * u1.i) + (self.j * u1.j) + (self.k * u1.k))
    
    def cross(self, u1):
        #following cross prod. formula using components.
        return Vector3d((self.j * u1.k - self.k * u1.j), (self.i * u1.k - self.k - u1.i), (self.i * u1.j - self.j * u1.i))
        


class Vector2d:
    def __init__(self, i=0, j=0):
        self.dim = 2
        self.i = i
        self.j = j
    
    def __add__(self, u1):
        return Vector2d(self.i + u1.i, self.j + u1.j)
    
    def __sub__(self, u1):
        return Vector2d(self.i - u1.i, self.j - u1.j)
    
    def __mul__(self, c1):
        ##Scalar multiplication. For cross and dot, see cross and dot.
        return Vector2d(self.i * c1, self.j * c1)
    
    def __neg__(self):
        return Vector2d(-self.i, -self.j)
    
    def __div__(self, c1):
        #I really don't like scalar division. Please just multiply by a fractional scalar.
        if c1 != 0:
            return Vector2d(self.i / c1, self.j / c1)
        else:
            return None
        
    def norm(self):
        return math.sqrt((self.i * self.i) + (self. j * self.j))

    def cross(self, u1):
        return ((self.i * u1.i) + (self.j * u1.j))
    
    def dot(self, u1):
        #will return a 3d vector
        return Vector3d((0), (0), (self.i * u1.j - self.j * u1.i))
