#Seth's Vector Classes
#2d and 3d

import math

class Vector2d:
    def __init__(self, i=0, j=0):
        self.dim = 2
        self.v1 = i
        self.v2 = j
    
    def __add__(self, u1):
        return Vector2d(self.v1 + u1.v1, self.v2 + u1.v2)
    
    def __sub__(self, u1):
        return Vector2d(self.v1 - u1.v1, self.v2 - u1.v2)
    
    def __mul__(self, c1):
        ##Scalar multiplication. For cross and dot, see cross and dot.
        return Vector2d(self.v1 * c1, self.v2 * c1)
    
    def __neg__(self):
        return Vector2d(-self.v1, -self.v2)
    
    def __div__(self, c1):
        #I really don't like scalar division. Please just multiply by a fractional scalar.
        if c1 != 0:
            return Vector2d(self.v1 / c1, self.v2 / c1)
        else:
            return None
        
    def norm(self):
        return math.sqrt((self.v1 * self.v1) + (self. v2 * self.v2))

    def cross(self, u1):
        return ((self.v1 * u1.v1) + (self.v2 * u1.v2))
    
    def dot(self, u1):
        #must implement vector3d
        pass
