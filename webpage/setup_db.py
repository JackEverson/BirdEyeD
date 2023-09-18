import os
import sqlalchemy
import sys
import werkzeug.security 

from sqlalchemy import create_engine, text

def setup_db(engine):

    with engine.begin() as conn:
        conn.execute(text("CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT NOT NULL, hash TEXT NOT NULL)"))
        conn.execute(text("INSERT INTO users (username, hash) VALUES (:username, :hash)"), [{"username": "sushi", "hash": "pbkdf2:sha256:600000$Sl9BZRT8KqWJvCRD$76c42623c2310193e5dc30530aeb4444b5098fad3f3ad2a327878c5498ecd42e "}])


def print_db():
    with engine.connect() as conn:
            result = conn.execute(text("SELECT * FROM users"))
            for row in result:
                print(f"user: {row.username}, hash: {row.hash}")


if __name__ == '__main__':

    engine = create_engine("sqlite:///bird.db", echo=True)

    if os.path.isfile('./bird.db'):
        print("Found user database")
        print_db()
        sys.exit("Database already created")        
    
    setup_db(engine)
    print_db()
    sys.exit(0)

