from functools import total_ordering
from datetime import date

@total_ordering
class Person:
    def __init__(self, person_id: int, name: str, age: int, city: str, male: bool = True) -> None:
        self.person_id = person_id
        self.name = name
        self.age = age
        self.male = male
        self.city = city

    def __str__(self) -> str:
        return f"#{self.person_id}: {self.name} ({self.age}, {self.male}, {self.city})"

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Person) and self.person_id == o.person_id

    def __lt__(self, o: object) -> bool:
        if not isinstance(o, Person):
            return NotImplemented
        return self.person_id < o.person_id

    def __hash__(self) -> int:
        return hash(self.person_id)


@total_ordering
class Movie:
    def __init__(self, movie_id: int, title: str, year: int, genre: str) -> None:
        self.movie_id = movie_id
        self.title = title
        self.year = year
        self.genre = genre

    def __str__(self) -> str:
        return f"#{self.movie_id}: {self.title} ({self.year}) - {self.genre}"

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Movie) and self.movie_id == o.movie_id

    def __lt__(self, o: object) -> bool:
        if not isinstance(o, Movie):
            return NotImplemented
        return self.movie_id < o.movie_id

    def __hash__(self) -> int:
        return hash(self.movie_id)
    

@total_ordering
class Review:
    def __init__(self, review_id: int, person_id: int, movie_id: int, rating: int, text: str, date: date) -> None:
        self.review_id = review_id
        self.person_id = person_id
        self.movie_id = movie_id
        self.rating = rating
        self.text = text
        self.date = date

    def __str__(self) -> str:
        return f"#{self.review_id}: Person {self.person_id} -> Movie {self.movie_id} | Rating: {self.rating} | Date: {self.date}"

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Review) and self.review_id == o.review_id

    def __lt__(self, o: object) -> bool:
        if not isinstance(o, Review):
            return NotImplemented
        return self.review_id < o.review_id

    def __hash__(self) -> int:
        return hash(self.review_id)

