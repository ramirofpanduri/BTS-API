from flask import Flask
from routes.book import books_bp
from routes.category import categories_bp


app = Flask(__name__)

app.register_blueprint(books_bp)
app.register_blueprint(categories_bp)

if __name__ == '__main__':
    app.run()
