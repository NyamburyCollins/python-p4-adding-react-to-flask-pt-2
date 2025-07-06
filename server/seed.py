#!/usr/bin/env python3

#!/usr/bin/env python3

from random import choice as rc
from faker import Faker

from server import create_app  # Import the app factory
from server.models import db, Movie

fake = Faker()

app = create_app()  # Create the app instance

def make_movies():
    print("Deleting existing movies...")
    Movie.query.delete()

    movies = []
    for i in range(50):
        m = Movie(title=fake.sentence(nb_words=4).title())
        movies.append(m)

    db.session.add_all(movies)
    db.session.commit()
    print("Movies seeded successfully!")

if __name__ == '__main__':
    with app.app_context():  # Correct context for the app factory
        # Optional safety check
        db.create_all()  # Ensure tables exist
        make_movies()
