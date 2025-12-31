# Import necessary libraries
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Create a new Flask application
app = Flask(__name__)

# Configure the application to use SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///learning_project.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define a route for the home page
@app.route('/')
def home():
    # Render the home page template
    return render_template('home.html')

# Run the application if this script is executed
if __name__ == '__main__':
    app.run(debug=True)