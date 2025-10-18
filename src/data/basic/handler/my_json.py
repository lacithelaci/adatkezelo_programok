import json
import os
from dataclasses import asdict
from datetime import datetime, date
from typing import List, cast, Type

from data.basic.model_dataclasses import Person, Movie, Review


def write_people(people: list[Person], path: str,
                 file_name: str = "people",
                 extension: str = ".json",
                 pretty: bool = True) -> None:
    with open(os.path.join(path, file_name + extension), "w") as file:
        json.dump(
            [person.__dict__ for person in people],
            file, indent=2 if pretty else None)


def read_people(path: str, file_name: str = "people",
                extension: str = ".json") -> list[Person]:
    with open(os.path.join(path, file_name + extension)) as file:
        def convert(d: dict) -> Person:
            return Person(**d)

        return json.load(file, object_hook=lambda d: Person(**d))


def write_movies(movies: list[Movie], path: str,
                 file_name: str = "movie",
                 extension: str = ".json",
                 pretty: bool = True) -> None:
    with open(os.path.join(path, file_name + extension), "w") as file:
        json.dump(
            [movie.__dict__ for movie in movies],
            file, indent=2 if pretty else None)


def read_movies(path: str, file_name: str = "movie",
                extension: str = ".json") -> list[Movie]:
    with open(os.path.join(path, file_name + extension)) as file:
        def convert(d: dict) -> Movie:
            return Movie(**d)

        return json.load(file, object_hook=lambda d: Movie(**d))


def write_reviews(reviews: List[Review], path: str, file_name: str = "review", extension: str = ".json",
                  pretty=True) -> None:
    file_name = file_name if file_name is not None else "review"
    extension = extension if extension is not None else ".json"

    def default_converter(o):
        if isinstance(o, date):
            return o.isoformat()
        raise TypeError(f"Type {type(o)} not serializable")

    with open(os.path.join(path, file_name + extension), "w", encoding="utf-8") as file:
        json.dump(
            [asdict(review) for review in reviews],
            file,
            indent=2 if pretty else None,
            default=default_converter
        )


def read_reviews(path: str, file_name: str = "review", extension: str = ".json") -> List[Review]:
    file_name = file_name if file_name is not None else "review"
    extension = extension if extension is not None else ".json"

    with open(os.path.join(path, file_name + extension), "r", encoding="utf-8") as file:
        docs = json.load(file)

    reviews = []
    for doc in docs:
        parsed_date = datetime.strptime(doc["date"], "%Y-%m-%d").date() if isinstance(doc["date"], str) else doc["date"]
        reviews.append(
            Review(
                review_id=doc["review_id"],
                person_id=doc["person_id"],
                movie_id=doc["movie_id"],
                rating=doc["rating"],
                text=doc["text"],
                date=parsed_date
            )
        )
    return reviews


def write(entities: list[object], path: str,
          file_name: str | None = None,
          extension: str = ".json",
          pretty: bool = True) -> None:
    if not entities:
        raise ValueError("Cannot write empty entity list")

    first = entities[0]

    if isinstance(first, Person):
        file_name = file_name or "people"
        write_people([cast(Person, e) for e in entities], path,
                     file_name=file_name, extension=extension, pretty=pretty)

    elif isinstance(first, Movie):
        file_name = file_name or "movie"
        write_movies([cast(Movie, e) for e in entities], path,
                     file_name=file_name, extension=extension, pretty=pretty)

    elif isinstance(first, Review):
        file_name = file_name or "review"
        write_reviews([cast(Review, e) for e in entities], path,
                      file_name=file_name, extension=extension, pretty=pretty)

    else:
        raise RuntimeError(f"Unknown entity type: {type(first).__name__}")


def read(path: str,
         file_name: str | None = None,
         extension: str = ".json") -> list[object]:
    if file_name is None:
        raise ValueError("File name must be provided for automatic type detection")

    if "people" in file_name:
        return read_people(path, file_name=file_name, extension=extension)
    elif "movie" in file_name:
        return read_movies(path, file_name=file_name, extension=extension)
    elif "review" in file_name:
        return read_reviews(path, file_name=file_name, extension=extension)
    else:
        raise RuntimeError(f"Unknown file type: {file_name}")

