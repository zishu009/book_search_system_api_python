from flask import request, jsonify
from models import db, Book
from schemas import book_schema, books_schema, prompt_schema
import random

def configure_routes(app):
    # Fetch all the books
    @app.route('/books', methods=['GET'])
    def get_books():
        books = Book.query.all()
        return jsonify(books_schema.dump(books)), 200

    # add new book into existing Book table
    @app.route('/add_book', methods=['POST'])
    def add_book():
        data = request.get_json()

        # Validate required fields
        required_fields = ['title', 'author', 'genre', 'year']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing field: {field}"}), 400


        title = data.get('title')
        author = data.get('author')
       
        # Check if the book already exists
        existing_book = Book.query.filter_by(title=title, author=author).first()
        if existing_book:
            return jsonify({"message": "Book with the same title and author already exists."}), 409

        new_book = Book(
            title=data['title'],
            author=data['author'],
            genre=data['genre'],
            year=data['year']
        )

        db.session.add(new_book)
        db.session.commit()

        return jsonify(book_schema.dump(new_book)), 201


    # fetch the records based on genre
    @app.route('/books/genre/<genre>', methods=['GET'])
    def get_books_by_genre(genre):
        # books = Book.query.filter_by(genre=genre).all()
        books = Book.query.filter(Book.genre.ilike(f"%{genre}%")).all()
        if not books:
            return jsonify({"message": f"No books found in genre '{genre}'"}), 404
        return jsonify(books_schema.dump(books)), 200

    # count the no. of books of a specific author
    @app.route('/books/author/<author>', methods=['GET'])
    def count_books_by_author(author):
        count = Book.query.filter(Book.author.ilike(f"%{author}%")).count()
        return jsonify({"author": author, "book_count": count}), 200


    # books records published after 2015
    @app.route('/books/recent', methods=['GET'])
    def get_books_after_2015():
        """API for books published after 2015"""
        recent_books = Book.query.filter(Book.year > 2015).all()
        if not recent_books:
            return jsonify({"message": "No books found published after 2015."}), 404
        return jsonify(books_schema.dump(recent_books)), 200


    # prompt api based on prompt you will get recommended books 
    @app.route('/query', methods=['POST'])
    def suggest_book():
        data = request.get_json()
    
        # Validate prompt input
        errors = prompt_schema.validate(data)
        if errors:
            return jsonify(errors), 400

        user_prompt = data['prompt'].lower()  # Make it lowercase for easier matching

        # Some simple keyword matching
        keywords = ['science fiction', 'space', 'science', 'personal finance', 'romance', 'history', 'technology', 'adventure', 'fantasy']

        matched_keyword = None
        for keyword in keywords:
            if keyword in user_prompt:
                matched_keyword = keyword
                break

        if not matched_keyword:
            return jsonify({"response": "Sorry, could not understand your prompt. Try using simpler words."}), 400

        # Search books based on matched keyword (in genre or title)
        books = Book.query.filter(
            (Book.title.ilike(f"%{matched_keyword}%")) | (Book.genre.ilike(f"%{matched_keyword}%"))
        ).all()

        if not books:
            return jsonify({"response": "Sorry, no books found based on your prompt."}), 404

        # Pick a random matching book
        book = random.choice(books)

        # Generate response based on template
        response_text = f"Based on your interest in {matched_keyword}, I recommend reading '{book.title}' by {book.author}."

        return jsonify({"response": response_text}), 200