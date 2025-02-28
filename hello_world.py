from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the root URL ('/')
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Run the application if executed directly
if __name__ == '__main__':
    app.run()