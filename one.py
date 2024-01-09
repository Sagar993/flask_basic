from app import app, db, Publication, Book
from datetime import datetime

# Use the app's context
with app.app_context():
    # Create instances of Publication and add them to the database
    publications_data = [
        {"name": "Sagar"},
        {"name": "Another Publication"},
        # Add more data as needed
    ]

    for data in publications_data:
        publication = Publication(**data)
        db.session.add(publication)

    db.session.flush()  # Get the id of the newly inserted Publication

    # Create Book instances for each publication and add them to the session
    books_data = [
        {
            "title": "New Book 1",
            "author": "Author 1",
            "avg_rating": 4.5,
            "format": "Hardcover",
            "image": "book_image_1.jpg",
            "num_pages": 300,
            "pub_date": datetime.utcnow(),
            "pub_id": publication.id
        },
        {
            "title": "New Book 2",
            "author": "Author 2",
            "avg_rating": 4.0,
            "format": "Paperback",
            "image": "book_image_2.jpg",
            "num_pages": 250,
            "pub_date": datetime.utcnow(),
            "pub_id": publication.id
        },
        # Add more book data as needed
    ]

    for data in books_data:
        new_book = Book(**data)
        db.session.add(new_book)

    # Commit the changes to the database
    db.session.commit()

print("Data added to the database successfully.")
