from datetime import date
from dataclasses import dataclass, field

@dataclass(order=True)
class Person:
    person_id: int = field(hash=True)
    name: str = field(repr=True, compare=False)
    age: int = field(repr=True, compare=False)
    city: str = field(repr=True, compare=False)
    male: bool = field(default=True, repr=True, compare=False)


@dataclass(order=True)
class Movie:
    movie_id: int = field(hash=True)
    title: str = field(repr=True, compare=False)
    year: int = field(repr=True, compare=False)
    genre: str = field(repr=True, compare=False)


@dataclass(order=True)
class Review:
    review_id: int = field(hash=True)
    person_id: int = field(repr=True, compare=False)
    movie_id: int = field(repr=True, compare=False)
    rating: int = field(repr=True, compare=False)
    text: str = field(repr=True, compare=False)
    date: date = field(repr=True, compare=False) # type: ignore



