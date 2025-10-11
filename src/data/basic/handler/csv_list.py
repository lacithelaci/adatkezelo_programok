import csv
import typing
from datetime import datetime
import os
from typing import Type, cast

from data.basic.model_dataclasses import Person, Movie, Review


def write_people(people: list[Person], path: str, delimiter: str = ";") -> None:
    with open(os.path.join(path, "people.csv"), "w", newline="") as file:
        writer = csv.writer(file, delimiter=delimiter)
        for person in people:
            writer.writerow([person.person_id, person.name, person.age, person.city, person.male])


def read_people(path: str, file_name: str = "people.csv", delimiter: str = ";") -> list[Person]:
    with open(os.path.join(path, file_name if file_name is not None else "people.csv"), "r") as file:
        rows = csv.reader(file, delimiter=delimiter)
        lista = []
        for row in rows:
            if row[4] == 'True':
                lista.append(Person(int(row[0]), row[1], int(row[2]), row[3], bool(row[4])))
            else:
                lista.append(Person(int(row[0]), row[1], int(row[2]), row[3], False))
        return lista


def write_movies(movies: list[Movie], path: str, delimiter: str = ";") -> None:
    with open(os.path.join(path, "movie.csv"), "w", newline="") as file:
        writer = csv.writer(file, delimiter=delimiter)
        for movie in movies:
            writer.writerow([movie.movie_id, movie.title, movie.year, movie.genre])


def read_movies(path: str, file_name: str = "movie.csv", delimiter: str = ";") -> list[Movie]:
    with open(os.path.join(path, file_name if file_name is not None else "movie.csv"), "r") as file:
        rows = csv.reader(file, delimiter=delimiter)
        return [Movie(int(row[0]), row[1], int(row[2]), row[3], ) for row in rows]


def write_reviews(reviews: list[Review], path: str, delimiter: str = ";") -> None:
    with open(os.path.join(path, "reviews.csv"), "w", newline="") as file:
        writer = csv.writer(file, delimiter=delimiter)
        for review in reviews:
            writer.writerow(
                [review.review_id, review.person_id, review.movie_id, review.rating, review.text, review.date])


def read_reviews(path: str, file_name: str = "reviews.csv", delimiter: str = ";") -> list[Review]:
    with open(os.path.join(path, file_name if file_name is not None else "reviews.csv"), "r") as file:
        rows = csv.reader(file, delimiter=delimiter)
        return [Review(int(row[0]), int(row[1]), int(row[2]), int(row[3]), row[4],
                       datetime.strptime(row[5], "%Y-%m-%d").date()) for row in rows]


def read(entity_type: typing.Type[object], path: str, file_name: str = None, delimiter: str = ";") -> list[object]:
    if entity_type == Person:
        return read_people(path, file_name=file_name, delimiter=delimiter)
    elif entity_type == Movie:
        return read_movies(path, file_name=file_name, delimiter=delimiter)
    elif entity_type == Review:
        return read_reviews(path, file_name=file_name, delimiter=delimiter)
    else:
        raise RuntimeError("Unknown type of entity")


def write(entities: list[object], path: str, file_name: str = None, delimiter: str = ";") -> None:
    if isinstance(entities[0], Person):
        return write_people([typing.cast(Person, e) for e in entities], path, delimiter=delimiter)
    elif isinstance(entities[0], Movie):
        return write_movies([typing.cast(Movie, e) for e in entities], path, delimiter=delimiter)
    elif isinstance(entities[0], Review):
        return write_reviews([typing.cast(Review, e) for e in entities], path, delimiter=delimiter)
    else:
        raise RuntimeError("Unknown type of entity")


