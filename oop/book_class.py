class Book:
    def __init__(self, title, author, year):
        """Initialize a Book instance with title, author, and year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor that prints a message upon deletion of the object."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Return a string representation of the book for casual use."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Return an official string representation of the book for debugging."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

# Ensure that the code below only runs when this script is executed directly
if __name__ == "__main__":
    # Example code for testing purposes (remove this if not needed)
    my_book = Book("1984", "George Orwell", 1949)
    print(my_book)         # This should call __str__()
    print(repr(my_book))   # This should call __repr__()
    del my_book            # This should call __del__()
