
from abc import ABC, abstractmethod


class Item(ABC):

    def __init__(self, item_id, title, price):
        self.item_id = str(item_id).strip()
        self.title = str(title).strip()
        self.__price = price
        self.__borrow_date = None
        self.__is_borrowed = False

        if not self.item_id:
            raise ValueError("Item ID cannot be empty.")

        if not self.title:
            raise ValueError("Item title cannot be empty.")

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise ValueError("Price must be a valid number.")

        if value <= 0:
            raise ValueError("Price must be greater than zero.")

        self.__price = float(value)

    @property
    def borrow_date(self):
        return self.__borrow_date

    @property
    def is_borrowed(self):
        return self.__is_borrowed

    def checkout(self):
        from datetime import date

        if self.__is_borrowed:
            raise ValueError("This item is already checked out.")

        self.__borrow_date = date.today()
        self.__is_borrowed = True

    def return_item(self):
        from datetime import date

        if not self.__is_borrowed:
            raise ValueError("This item is not currently checked out.")

        days_borrowed = (date.today() - self.__borrow_date).days
        days_borrowed = max(1, days_borrowed)

        fee = self.calculate_fee(days_borrowed)

        self.__borrow_date = None
        self.__is_borrowed = False

        return fee

    @abstractmethod
    def calculate_fee(self, days_borrowed):
        pass

    @abstractmethod
    def display_metadata(self):
        pass

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} | ID: {self.item_id} | Status: {status}"

    def __repr__(self):
        return (
            f"{self.__class__.__name__}("
            f"item_id={self.item_id!r}, "
            f"title={self.title!r}, "
            f"price={self.price!r})"
        )

    def __eq__(self, other):
        if not isinstance(other, Item):
            return NotImplemented

        return (
            type(self) is type(other)
            and self.item_id == other.item_id
        )


class Book(Item):

    DAILY_FEE = 5.0

    def __init__(self, item_id, title, author, price):
        super().__init__(item_id, title, price)
        self.author = author.strip()

    def calculate_fee(self, days_borrowed):
        return max(0, days_borrowed) * self.DAILY_FEE

    def display_metadata(self):
        return (
            f"Type: Book | ID: {self.item_id} | "
            f"Title: {self.title} | Author: {self.author} | "
            f"Price: Rs. {self.price:.2f} | "
            f"Daily Fee: Rs. {self.DAILY_FEE:.2f}"
        )


class Magazine(Item):

    DAILY_FEE = 3.0

    def __init__(self, item_id, title, issue_number, price):
        super().__init__(item_id, title, price)
        self.issue_number = str(issue_number).strip()

    def calculate_fee(self, days_borrowed):
        return max(0, days_borrowed) * self.DAILY_FEE

    def display_metadata(self):
        return (
            f"Type: Magazine | ID: {self.item_id} | "
            f"Title: {self.title} | Issue: {self.issue_number} | "
            f"Price: Rs. {self.price:.2f} | "
            f"Daily Fee: Rs. {self.DAILY_FEE:.2f}"
        )


class DigitalMedia(Item):

    DAILY_FEE = 10.0

    def __init__(self, item_id, title, file_format, duration_minutes, price):
        super().__init__(item_id, title, price)
        self.file_format = file_format.strip().upper()

        if not isinstance(duration_minutes, int) or isinstance(duration_minutes, bool):
            raise ValueError("Duration must be a whole number.")

        if duration_minutes <= 0:
            raise ValueError("Duration must be greater than zero.")

        self.duration_minutes = duration_minutes

    def calculate_fee(self, days_borrowed):
        return max(0, days_borrowed) * self.DAILY_FEE

    def display_metadata(self):
        return (
            f"Type: Digital Media | ID: {self.item_id} | "
            f"Title: {self.title} | Format: {self.file_format} | "
            f"Duration: {self.duration_minutes} minutes | "
            f"Price: Rs. {self.price:.2f} | "
            f"Daily Fee: Rs. {self.DAILY_FEE:.2f}"
        )
