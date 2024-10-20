import math

class Shape:
    def area(self):
        """Raise NotImplementedError to indicate this method should be overridden."""
        raise NotImplementedError("Subclasses must implement this method.")

class Rectangle(Shape):
    def __init__(self, length, width):
        """Initialize the rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Override the area method to calculate the area of the rectangle."""
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        """Initialize the circle with radius."""
        self.radius = radius

    def area(self):
        """Override the area method to calculate the area of the circle."""
        return math.pi * (self.radius ** 2)

# Ensure that the code below only runs when this script is executed directly
if __name__ == "__main__":
    # Example code for testing purposes (remove this if not needed)
    shapes = [Rectangle(10, 5), Circle(7)]
    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

