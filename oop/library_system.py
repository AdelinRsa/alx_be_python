class Book:
    def __init__(self, title, author):
        """Initialize a Book instance with title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """Return a string representation of the book."""
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize an EBook instance with title, author, and file size."""
        super().__init__(title, author)  # Call the constructor of the base class
        self.file_size = file_size

    def __str__(self):
        """Return a string representation of the EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize a PrintBook instance with title, author, and page count."""
        super().__init__(title, author)  # Call the constructor of the base class
        self.page_count = page_count

    def __str__(self):
        """Return a string representation of the PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    def __init__(self):
        """Initialize the Library with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Add a Book, EBook, or PrintBook instance to the library."""
        self.books.append(book)

    def list_books(self):
        """Print details of each book in the library."""
        for book in self.books:
            print(book)  # Calls the __str__ method of each book instance

# Ensure that the code below only runs when this script is executed directly
if __name__ == "__main__":
    # Example code for testing purposes (remove this if not needed)
    library = Library()
    library.add_book(Book("Sample Book", "Sample Author"))
    library.list_books()

