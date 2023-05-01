# from flask import Blueprint, jsonify, abort, make_response
from app import db
from app.models.book import Book
from flask import Blueprint, jsonify, make_response, request, query



# hello_world_bp = Blueprint("hello_world", __name__)
books_bp = Blueprint("books", __name__, url_prefix="/books")

# @hello_world_bp.route("/hello-world", methods=["GET"])

# def say_hello_world():
#     my_beautiful_world = "Hello world!"
#     return my_beautiful_world

# @hello_world_bp.route("/hello/JSON", methods=['GET'])

# def say_hello_json():
#     return {
#         "name": "Ada Lovelace",
#         "message": "Hello!",
#         "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
#     }
    
# class Book:
#     def __init__(self, id, title, description):
#         self.id = id
#         self.title = title
#         self.description = description
        
# books = [Book(1, "Made Up Book", "Most excellent review and description."),
#          Book(2, "Great Book", "A Book on greatness, by the greatest"),
#          Book(3, "Best of books, worst of books", "It was the best of books and the worst of books.")]

def validate_book(book_id):
    try:
        book_id = int(book_id)
    except:
        abort(make_response({"message":f"book {book_id} invalid"}, 400))

    book = Book.query.get(book_id)

    if not book:
        abort(make_response({"message":f"book {book_id} not found"}, 404))

    return book
        
# @books_bp.route("", methods=["GET"])
# def handle_books():
#     books_response = []
#     for book in books:
#         books_response.append({
#             "id": book.id,
#             "title": book.title,
#             "description": book.description
#         })
#     return jsonify(books_response)

@books_bp.route("/<book_id>", methods=["GET"])
def read_one_book(book_id):
    book = validate_book(book_id)
    return {
                "id": book.id,
                "title": book.title,
                "description": book.description
            }

@books_bp.route('', methods=["GET"])
def read_all_books():
    books = Book.query.all()
    books_response = []
    for book in books:
            books_response.append({
                "id": book.id,
                "title": book.title,
                "description": book.description
            })
    return jsonify(books_response)
    
@books_bp.route('', methods=["POST"])
def create_book():
    request_body = request.get_json()
    new_book = Book(title=request_body['title'],
                        description=request_body['description'])
    db.session.add(new_book)
    db.session.commit()
    
    return make_response(f'Book {new_book.title} successfully created', 201)

@books_bp.route("/<book_id>", methods=["PUT"])
def update_book(book_id):
    book = validate_book(book_id)
    
    request_body = request.get_json()
    
    book.title = request_body["title"]
    book.description = request_body["description"]
    
    db.session.commit()
    
    return make_response(f"Book {book.id} successfully updated")

@books_bp.route("/<book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = validate_book(book_id)
    
    db.session.delete(book)
    db.session.commit()
    
    return make_response(f"Book #{book.id} successfully deleted")