from flask import Flask, Response, jsonify, request
import xml.etree.ElementTree as ET
app = Flask(__name__)
books = [ # Sample data
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"},
]
# GET request to fetch all books in XML format
@app.route('/books', methods=['GET'])
def get_books():
    root = ET.Element('books')
    for book in books:
        xml_book = ET.SubElement(root, 'book')
        xml_book.set('id', str(book['id']))
        title = ET.SubElement(xml_book, 'title')
        title.text = book['title']
        author = ET.SubElement(xml_book, 'author')
        author.text = book['author']
    xml_string = ET.tostring(root, encoding='utf-8')
    return Response(xml_string, mimetype='text/xml')
# GET request to fetch a specific book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if book:
        return jsonify(book)
    return jsonify({'message': 'Book not found'}), 404
# POST request to add a new book
@app.route('/books', methods=['POST'])
def add_book():
    new_book = {
        'id': len(books) + 1,
        'title': request.json['title'],
        'author': request.json['author']
}
    books.append(new_book)
    return jsonify(new_book), 201
if __name__ == '__main__':
    app.run(debug=True)
