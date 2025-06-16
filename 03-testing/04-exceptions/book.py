class Book:
    def __init__(self, title, isbn):
        if not title:
            raise RuntimeError("Invalid title")

        digits = [int(c) for c in isbn if c.isdigit()]
        if len(digits) != 13:
            raise RuntimeError("Invalid ISBN")

        total = 0
        for i, digit in enumerate(digits):
            if i % 2 == 0:
                total += digit
            else:
                total += 3 * digit

        if total % 10 != 0:
            raise RuntimeError("Invalid ISBN")

        self.__title = title
        self.__isbn = isbn

    @property
    def title(self):
        return self.__title

    @property
    def isbn(self):
        return self.__isbn
