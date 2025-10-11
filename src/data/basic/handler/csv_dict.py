import csv
import os
from datetime import datetime
from typing import cast, Type

from data.basic.model_dataclasses import Person, Movie, Review


def write_people(people: list[Person], path: str, file_name: str = "people",
                 extension: str = ".csv", heading: bool = True, delimiter: str = ";") -> None:
    file_name = file_name if file_name is not None else "people"
    extension = extension if extension is not None else ".csv"

    with open(os.path.join(path, file_name + extension), "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["person_id", "name", "age", "city", "male"], delimiter=delimiter)
        if heading:
            writer.writeheader()
        for person in people:
            writer.writerow(person.__dict__)


def read_people(path: str, file_name: str = "people", extension: str = ".csv", delimiter: str = ";") -> list[Person]:
    file_name = file_name if file_name is not None else "people"
    extension = extension if extension is not None else ".csv"

    with open(os.path.join(path, file_name + extension), "r", newline="") as file:
        rows: dict = csv.DictReader(file, delimiter=delimiter)
        return [
            Person(int(row["person_id"]), row["name"], int(row["age"]), row["city"], row["male"].lower() == "true") for
            row in rows
        ]


def write_movies(movies: list[Movie], path: str, file_name: str = "movie", extension: str = ".csv",
                 heading: bool = True, delimiter: str = ";") -> None:
    file_name = file_name if file_name is not None else "movie"
    extension = extension if extension is not None else ".csv"

    with open(os.path.join(path, file_name + extension), "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["movie_id", "title", "year", "genre"], delimiter=delimiter)
        if heading:
            writer.writeheader()
        for movie in movies:
            writer.writerow(movie.__dict__)


def read_movies(path: str, file_name: str = "movie", extension: str = ".csv", delimiter: str = ";") -> list[Movie]:
    file_name = file_name if file_name is not None else "movie"
    extension = extension if extension is not None else ".csv"

    with open(os.path.join(path, file_name + extension), "r") as file:
        rows: dict = csv.DictReader(file, delimiter=delimiter)
        return [Movie(int(row["movie_id"]), row["title"], int(row["year"]), row["genre"]) for row in rows]


def write_reviews(movies: list[Review], path: str, file_name: str = "reviews", extension: str = ".csv",
                  heading: bool = True, delimiter: str = ";") -> None:
    file_name = file_name if file_name is not None else "reviews"
    extension = extension if extension is not None else ".csv"

    with open(os.path.join(path, file_name + extension), "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["review_id", "person_id", "movie_id", "rating", "text", "date"],
                                delimiter=delimiter)
        if heading:
            writer.writeheader()
        for movie in movies:
            writer.writerow(movie.__dict__)


def read_reviews(path: str, file_name: str = "reviews", extension: str = ".csv", delimiter: str = ";") -> list[Review]:
    file_name = file_name if file_name is not None else "reviews"
    extension = extension if extension is not None else ".csv"

    with open(os.path.join(path, file_name + extension), "r") as file:
        rows: dict = csv.DictReader(file, delimiter=delimiter)
        return [
            Review(int(row["review_id"]), int(row["person_id"]), int(row["movie_id"]), int(row["rating"]), row["text"],
                   datetime.strptime(row["date"], "%Y-%m-%d").date()) for row in rows]


def write(entities: list[object], path: str, file_name: str = None, extension: str = None,
          heading: bool = True, delimiter: str = ";") -> None:
    if isinstance(entities[0], Person):
        return write_people([cast(Person, e) for e in entities], path, file_name=file_name, extension=extension,
                            heading=heading, delimiter=delimiter)
    elif isinstance(entities[0], Movie):
        return write_movies([cast(Movie, e) for e in entities], path, file_name=file_name, extension=extension,
                            heading=heading, delimiter=delimiter)
    elif isinstance(entities[0], Review):
        return write_reviews([cast(Review, e) for e in entities], path, file_name=file_name, extension=extension,
                             heading=heading, delimiter=delimiter)
    else:
        raise RuntimeError("Unknown type of entity")


def read(entity_type: Type[object], path: str, file_name: str = None, delimiter: str = ";") -> list[object]:
    if entity_type == Person:
        return read_people(path, file_name=file_name, delimiter=delimiter)
    elif entity_type == Movie:
        return read_movies(path, file_name=file_name, delimiter=delimiter)
    elif entity_type == Review:
        return read_reviews(path, file_name=file_name, delimiter=delimiter)
    else:
        raise RuntimeError("Unknown type of entity")

