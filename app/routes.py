from flask import Blueprint, jsonify

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
    
class Book:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description
        
books = [Book(1, "Made Up Book", "Most excellent review and description."),
         Book(2, "Great Book", "A Book on greatness, by the greatest"),
         Book(3, "Best of books, worst of books", "It was the best of books and the worst of books.")]

@books_bp.route("", methods=["GET"])
def handle_books():
    books_response = []
    for book in books:
        books_response.append({
            "id": book.id,
            "title": book.title,
            "description": book.description
        })
    return jsonify(books_response)