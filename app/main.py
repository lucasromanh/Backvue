from app import app
from contacts import contacts
import os


app.register_blueprint(contacts)

if __name__ == "__main__":
    app.run(port=int(os.environ.get('PORT', '3000')), debug=True)
