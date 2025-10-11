from faker import Faker
import random
from data.basic.model_dataclasses import Review, Person, Movie
import datetime


# ───────────────────────────────
# Személyek generálása
# ───────────────────────────────
def generate_people(n: int,
                    male_ratio: float = 0.5,
                    locale: str = "en_US",
                    unique: bool = True,  # Ne ismétlődjenek a nevek
                    min_age: int = 10,
                    max_age: int = 99) -> list[Person]:
    fake = Faker(locale)
    people = []
    generator = fake.unique if unique else fake  # Ez a sor biztosítja, hogy ne legyenek duplikált nevek

    for i in range(1, n + 1):
        male = random.random() < male_ratio
        name = generator.name_male() if male else generator.name_female()
        age = random.randint(min_age, max_age)
        city = generator.city()
        people.append(Person(i, name, age, city, male))

    return people


# ───────────────────────────────
# Filmek generálása
# ───────────────────────────────

def generate_movies(n: int,
                    locale: str = "en_US",
                    unique: bool = True,
                    year_min: int = 1970,
                    year_max: int = datetime.datetime.now().year,
                    genres: list[str] = None) -> list[Movie]:
    fake = Faker(locale)
    movies = []
    generator = fake.unique if unique else fake

    if genres is None:
        genres = ["Action", "Drama", "Comedy", "Horror", "Sci-Fi", "Fantasy", "Romance"]

    for i in range(1, n + 1):
        title = generator.sentence(nb_words=3).strip(".")
        year = random.randint(year_min, year_max)
        genre = random.choice(genres)
        movies.append(Movie(i, title, year, genre))

    return movies


# ───────────────────────────────
# Vélemények generálása
# ───────────────────────────────
def generate_reviews(n: int,
                     people: list[Person],
                     movies: list[Movie],
                     locale: str = "en_US",
                     unique: bool = True,
                     min_rating: int = 1,
                     max_rating: int = 5) -> list[Review]:
    fake = Faker(locale)
    reviews = []
    generator = fake.unique if unique else fake

    for i in range(1, n + 1):
        person = random.choice(people)
        movie = random.choice(movies)
        rating = random.randint(min_rating, max_rating)
        text = generator.text(max_nb_chars=200)
        date = generator.date_this_year()
        reviews.append(Review(i, person.person_id, movie.movie_id, rating, text, date))

    return reviews


# ───────────────────────────────
# Tesztelés
# ───────────────────────────────
if __name__ == "__main__":
    people = generate_people(5, male_ratio=0.6, locale="hu_HU", unique=True)
    movies = generate_movies(5, locale="en_US", year_min=1990, year_max=2025)
    reviews = generate_reviews(10, people, movies)

    print("Emberek:")
    for p in people:
        print(p)

    print("Filmek:")
    for m in movies:
        print(m)

    print("\nVélemények:")
    for r in reviews:
        print(r)


