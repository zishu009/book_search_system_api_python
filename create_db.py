from app import create_app
from models import db, Book

app = create_app()

def seed_database():
    with app.app_context():
        # Clear existing data
        Book.query.delete()
        
        # Add sample books
        books = [
            Book(title="Cosmos", author="Carl Sagan", genre="science", year=1980),
            Book(title="A Brief History of Time", author="Stephen Hawking", genre="science", year=1988),
            Book(title="1984", author="George Orwell", genre="dystopian fiction", year=1949),
            Book(title="The Martian", author="Andy Weir", genre="science fiction", year=2014),
            Book(title="Dune", author="Frank Herbert", genre="science fiction", year=1965),
            Book(title="The Hobbit", author="J.R.R. Tolkien", genre="fantasy", year=1937),
            Book(title="Sapiens", author="Yuval Noah Harari", genre="history", year=2011),
            Book(title="The Psychology of Money", author="Morgan Housel", genre="personal finance", year=2020),
            Book(title="Astrophysics for People in a Hurry", author="Neil deGrasse Tyson", genre="science", year=2017),
            Book(title="The Lord of the Rings", author="J.R.R. Tolkien", genre="fantasy", year=1954),
        ]
        
        db.session.add_all(books)
        db.session.commit()

if __name__ == '__main__':
    seed_database()