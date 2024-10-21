from flask import Flask
from database import init_db,db
from Routes import register_routes
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')



app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY  
# Initialize the database
init_db(app)

# Register routes from external file
register_routes(app)

# # Drop all tables
# with app.app_context():
#     db.drop_all()
#     print("All tables have been dropped successfully!")
if __name__ == '__main__':
    app.run(debug=True)
