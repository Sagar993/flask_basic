from app import app, db, Book,Publication

# Assuming your Flask application instance is named 'app'
# and your SQLAlchemy instance is named 'db'
with app.app_context():
    # Query all records from the 'Book' table
   result=Publication.query.filter_by(name='Another Publication').first()
   final_result=Book.query.filter_by(pub_id=result.id).all()
   book1=Book.query.filter_by(pub_id=15).delete()
   book=Publication.query.get(15)
   book.id
   db.session.delete(book)
   db.session.commit()