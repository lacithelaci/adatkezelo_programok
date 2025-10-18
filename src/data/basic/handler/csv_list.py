import csv
import typing
from datetime import datetime
import os
from typing import cast

from data.basic.model_dataclasses import Person, Movie, Review


# --- Alap write/read függvények ---

def write_people(people: list[Person], path: str, file_name: str = "people",
                 extension: str = ".csv", delimiter: str = ";") -> None:
    file_path = os.path.join(path, f"{file_name}{extension}")
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file, delimiter=delimiter)
        for person in people:
            writer.writerow([person.person_id, person.name, person.age, person.city, person.male])


def read_people(path: str, file_name: str = "people", extension: str = ".csv",
                delimiter: str = ";") -> list[Person]:
    file_path = os.path.join(path, f"{file_name}{extension}")
    with open(file_path, "r") as file:
        rows = csv.reader(file, delimiter=delimiter)
        result = []
        for row in rows:
            male = True if row[4] == "True" else False
            result.append(Person(int(row[0]), row[1], int(row[2]), row[3], male))
        return result


def write_movies(movies: list[Movie], path: str, file_name: str = "movie",
                 extension: str = ".csv", delimiter: str = ";") -> None:
    file_path = os.path.join(path, f"{file_name}{extension}")
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file, delimiter=delimiter)
        for movie in movies:
            writer.writerow([movie.movie_id, movie.title, movie.year, movie.genre])


def read_movies(path: str, file_name: str = "movie", extension: str = ".csv",
                delimiter: str = ";") -> list[Movie]:
    file_path = os.path.join(path, f"{file_name}{extension}")
    with open(file_path, "r") as file:
        rows = csv.reader(file, delimiter=delimiter)
        return [Movie(int(row[0]), row[1], int(row[2]), row[3]) for row in rows]


def write_reviews(reviews: list[Review], path: str, file_name: str = "review",
                  extension: str = ".csv", delimiter: str = ";") -> None:
    file_path = os.path.join(path, f"{file_name}{extension}")
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file, delimiter=delimiter)
        for review in reviews:
            writer.writerow([
                review.review_id, review.person_id, review.movie_id,
                review.rating, review.text, review.date
            ])


def read_reviews(path: str, file_name: str = "review", extension: str = ".csv",
                 delimiter: str = ";") -> list[Review]:
    file_path = os.path.join(path, f"{file_name}{extension}")
    with open(file_path, "r") as file:
        rows = csv.reader(file, delimiter=delimiter)
        return [
            Review(
                int(row[0]), int(row[1]), int(row[2]), int(row[3]),
                row[4], datetime.strptime(row[5], "%Y-%m-%d").date()
            )
            for row in rows
        ]


# --- Automatikus write / read wrapper-ek ---

def write(entities: list[object], path: str,
          file_name: str | None = None,
          extension: str = ".csv",
          delimiter: str = ";") -> None:
    if not entities:
        raise ValueError("Cannot write empty entity list")

    first = entities[0]

    if isinstance(first, Person):
        file_name = file_name or "people"
        write_people([cast(Person, e) for e in entities], path,
                     file_name=file_name, extension=extension, delimiter=delimiter)

    elif isinstance(first, Movie):
        file_name = file_name or "movie"
        write_movies([cast(Movie, e) for e in entities], path,
                     file_name=file_name, extension=extension, delimiter=delimiter)

    elif isinstance(first, Review):
        file_name = file_name or "review"
        write_reviews([cast(Review, e) for e in entities], path,
                      file_name=file_name, extension=extension, delimiter=delimiter)

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
