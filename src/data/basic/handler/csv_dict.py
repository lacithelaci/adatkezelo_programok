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


def write(entities: list[object], path: str,
          file_name: str | None = None,
          extension: str = ".csv",
          heading: bool = True,
          delimiter: str = ";") -> None:
    if not entities:
        raise ValueError("Cannot write empty entity list")

    first = entities[0]

    if isinstance(first, Person):
        file_name = file_name or "people"
        write_people([cast(Person, e) for e in entities], path,
                     file_name=file_name, extension=extension,
                     heading=heading, delimiter=delimiter)

    elif isinstance(first, Movie):
        file_name = file_name or "movie"
        write_movies([cast(Movie, e) for e in entities], path,
                     file_name=file_name, extension=extension,
                     heading=heading, delimiter=delimiter)

    elif isinstance(first, Review):
        file_name = file_name or "review"
        write_reviews([cast(Review, e) for e in entities], path,
                      file_name=file_name, extension=extension,
                      heading=heading, delimiter=delimiter)

    else:
        raise RuntimeError(f"Unknown entity type: {type(first).__name__}")


def read(path: str,
         file_name: str | None = None,
         extension: str = ".csv",
         delimiter: str = ";") -> list[object]:
    if file_name is None:
        raise ValueError("File name must be provided for automatic type detection")

    if "people" in file_name:
        return read_people(path, file_name=file_name, extension=extension, delimiter=delimiter)
    elif "movie" in file_name:
        return read_movies(path, file_name=file_name, extension=extension, delimiter=delimiter)
    elif "review" in file_name:
        return read_reviews(path, file_name=file_name, extension=extension, delimiter=delimiter)
    else:
        raise RuntimeError(f"Unknown file type: {file_name}")
