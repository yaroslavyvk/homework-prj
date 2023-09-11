class Products:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Book(Products):
    def __init__(self, name, price, quantity, author):
        super().__init__(name, price, quantity)
        self.author = author

    def read(self):
        return (f'The name of book {self.name}, price {self.price}$, quantity {self.quantity} and author {self.author}')


book1 = Book('"The Catcher in the Rye"', 10, 1, 'J.D. Salinger')
book1.read()
