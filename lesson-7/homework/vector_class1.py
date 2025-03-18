import math


class Vector:
    def __init__(self, *components):
        """Initialize an n-dimensional vector."""
        self.components = tuple(components)

    def __str__(self):
        """Return string representation of the vector."""
        return f"Vector{self.components}"

    def __repr__(self):
        """Return string representation of the vector."""
        return f"Vector{self.components}"

    def __add__(self, other):
        """Vector addition."""
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimension for addition.")
        return Vector(*[a + b for a, b in zip(self.components, other.components)])

    def __sub__(self, other):
        """Vector subtraction."""
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimension for subtraction.")
        return Vector(*[a - b for a, b in zip(self.components, other.components)])

    def __mul__(self, scalar):
        """Scalar multiplication."""
        if not isinstance(scalar, (int, float)):
            raise TypeError("Scalar must be a number.")
        return Vector(*[scalar * x for x in self.components])

    def __rmul__(self, scalar):
        """Support scalar * vector multiplication."""
        return self.__mul__(scalar)

    def dot(self, other):
        """Dot product of two vectors."""
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimension for dot product.")
        return sum(a * b for a, b in zip(self.components, other.components))

    def magnitude(self):
        """Compute the magnitude (length) of the vector."""
        return math.sqrt(sum(x ** 2 for x in self.components))

    def normalize(self):
        """Return the unit vector (normalized vector)."""
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector.")
        return Vector(*[x / mag for x in self.components])



v1 = Vector(3, 4)
v2 = Vector(1, 2)
print(v1 + v2)
print(v1 - v2)
print(v1 * 2)
print(2 * v1)
print(v1.dot(v2))
print(v1.magnitude())
print(v1.normalize())
