class Book:
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        raise AttributeError("Название книги нельзя изменить.")

    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, value: str):
        raise AttributeError("Автора книги нельзя изменить.")

    def __str__(self):
        return f"{self.__class__.__name__}: «{self.name}» by {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}', author='{self.author}')"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом.")
        self._pages = value

    def __str__(self):
        return f"Печатная книга: «{self.name}» by {self.author}, {self.pages} стр."

    def __repr__(self):
        return f"PaperBook(name='{self.name}', author='{self.author}', pages={self.pages})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, value: float):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом.")
        self._duration = value

    def __str__(self):
        return f"Аудиокнига: «{self.name}» by {self.author}, длительность {self.duration:.2f} ч."

    def __repr__(self):
        return f"AudioBook(name='{self.name}', author='{self.author}', duration={self.duration:.2f})"

paper_book = PaperBook("Война и мир", "Лев Толстой", 1225)
audio_book = AudioBook("Преступление и наказание", "Федор Достоевский", 25.7)

print(paper_book)       # Печатная книга: «Война и мир» by Лев Толстой, 1225 стр.
print(audio_book)       # Аудиокнига: «Преступление и наказание» by Федор Достоевский, длительность 25.70 ч.

print(repr(paper_book)) # PaperBook(name='Война и мир', author='Лев Толстой', pages=1225)
print(repr(audio_book)) # AudioBook(name='Преступление и наказание', author='Федор Достоевский', duration=25.700000)