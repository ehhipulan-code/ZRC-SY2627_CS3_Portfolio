
class Publication:
    def __init__(self, title: str, author: str):
        self.__title = title
        self.__author = author

    # Getters and setters
    def get_title(self) -> str:
        return self.__title

    def set_title(self, title: str):
        self.__title = title

    def get_author(self) -> str:
        return self.__author

    def set_author(self, author: str):
        self.__author = author

    def display_info(self):
        print(f"Title: {self.__title}, Author: {self.__author}")


class Book(Publication):
    def __init__(self, title: str, author: str, number_pages: int):
        super().__init__(title, author)
        self.__number_of_pages = 1
        self.set_number_of_pages(number_pages)

    def get_number_of_pages(self) -> int:
        return self.__number_of_pages

    def set_number_of_pages(self, number_pages: int):
        if isinstance(number_pages, int) and not isinstance(number_pages, bool) and number_pages > 0:
            self.__number_of_pages = number_pages
        else:
            print("The number of pages must be positive.")


class Magazine(Publication):
    def __init__(self, title: str, author: str, issue_number: int):
        super().__init__(title, author)
        self.__issue_number = 1
        self.set_issue_number(issue_number)

    def get_issue_number(self) -> int:
        return self.__issue_number

    def set_issue_number(self, issue_number: int):
        if isinstance(issue_number, int) and not isinstance(issue_number, bool) and issue_number > 0:
            self.__issue_number = issue_number
        else:
            print("The issue number must be positive.")


# Create two Publication objects
publication1 = Publication("The Little Prince", "Antoine de Saint-Exupery")
publication2 = Publication("Noli Me Tangere", "Jose Rizal")

# Create two Book objects
book1 = Book("Harry Potter", "J.K. Rowling", 350)
book2 = Book("The Hobbit", "J.R.R. Tolkien", 310)

# Create two Magazine objects
magazine1 = Magazine("National Geographic", "Susan Goldberg", 25)
magazine2 = Magazine("TIME", "Sam Jacobs", 48)


# Display Publication information
print("=== PUBLICATIONS ===")
publication1.display_info()
publication2.display_info()

# Display Book information
print("\n=== BOOKS ===")
book1.display_info()
print(f"Number of pages: {book1.get_number_of_pages()}")

book2.display_info()
print(f"Number of pages: {book2.get_number_of_pages()}")

# Display Magazine information
print("\n=== MAGAZINES ===")
magazine1.display_info()
print(f"Issue number: {magazine1.get_issue_number()}")

magazine2.display_info()
print(f"Issue number: {magazine2.get_issue_number()}")


# Test data validation
print("\n=== VALIDATION TESTS ===")
book1.set_number_of_pages(0)
magazine1.set_issue_number(-2)