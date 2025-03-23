# import json
# import mysql.connector
# from datetime import datetime

# # **MySQL Database Connection**
# conn = mysql.connector.connect(
#     host="localhost",       # Use "localhost" if running MySQL locally
#     user="root",            # Your MySQL username (default is "root")
#     password="root",  # Your MySQL password
#     database="movie_database",   # Replace with your actual database name
#     charset="utf8"  # Use utf8 if utf8mb4 causes issues
# )

# cursor = conn.cursor()

# # **Fetch Existing Directors from the Database**
# cursor.execute("SELECT director_id, name FROM directors;")
# director_ids = {name: director_id for director_id, name in cursor.fetchall()}  # Dictionary mapping

# # Load JSON data
# file_path = "movies-250.json"  # Change to your file path
# with open(file_path, "r") as f:
#     data = json.load(f)

# movies = data.get("movies", [])  # Extract movie list
# next_movie_id = 1  # Auto-incrementing movie ID

# # Print SQL queries to the terminal
# print("\n-- Create movies table")
# print("CREATE TABLE movies (")
# print("    movie_id INT PRIMARY KEY AUTO_INCREMENT,")
# print("    name VARCHAR(255) NOT NULL,")
# print("    release_date DATE,")
# print("    director_id INT,")
# print("    FOREIGN KEY (director_id) REFERENCES directors(director_id) ON DELETE CASCADE")
# print(");\n")

# print("-- Insert movies")
# for movie in movies:
#     title = movie.get("Title", "Unknown").replace("'", "''")
#     release_date = movie.get("Released", "")
#     director = movie.get("Director", "").strip()

#     # Convert release date format
#     try:
#         date_obj = datetime.strptime(release_date, "%d %b %Y")
#         release_date = date_obj.strftime("%Y-%m-%d")
#     except ValueError:
#         release_date = None

#     # Get `director_id` from the MySQL database
#     director_id = director_ids.get(director, "NULL")  # If not found, store as NULL

#     # Insert Movie Query
#     release_date_value = f"'{release_date}'" if release_date else "NULL"
#     print(f"INSERT INTO movies (movie_id, name, release_date, director_id) "
#           f"VALUES ({next_movie_id}, '{title}', {release_date_value}, {director_id});")

#     next_movie_id += 1

# # Close database connection
# cursor.close()
# conn.close()


import json
import mysql.connector
from datetime import datetime

# **Connect to MySQL Database**
conn = mysql.connector.connect(
    host="localhost",       # Use "localhost" if running MySQL locally
    user="root",            # Your MySQL username
    password="root",  # Your MySQL password
    database="movie_database",   # Your actual database name
    charset="utf8"  # Use utf8 instead of utf8mb4 to avoid errors
)

cursor = conn.cursor()

# **Fetch Existing Directors from MySQL**
cursor.execute("SELECT director_id, name FROM directors;")
director_ids = {name: director_id for director_id, name in cursor.fetchall()}  # Dictionary mapping

# **Fetch Existing Genres from MySQL**
cursor.execute("SELECT genre_id, name FROM genres;")
genre_ids = {name: genre_id for genre_id, name in cursor.fetchall()}  # Dictionary mapping

# **Load JSON Data**
file_path = "movies-250.json"  # Change to your actual file path
with open(file_path, "r") as f:
    data = json.load(f)

movies = data.get("movies", [])  # Extract movie list
next_movie_id = 1  # Auto-incrementing movie ID

# **Print SQL Queries**
print("\n-- Create movies table")
print("CREATE TABLE movies (")
print("    movie_id INT PRIMARY KEY AUTO_INCREMENT,")
print("    name VARCHAR(255) NOT NULL,")
print("    release_date DATE,")
print("    director_id INT,")
print("    FOREIGN KEY (director_id) REFERENCES directors(director_id) ON DELETE CASCADE")
print(");\n")

print("-- Create movie_genres table")
print("CREATE TABLE movie_genres (")
print("    movie_id INT,")
print("    genre_id INT,")
print("    PRIMARY KEY (movie_id, genre_id),")
print("    FOREIGN KEY (movie_id) REFERENCES movies(movie_id) ON DELETE CASCADE,")
print("    FOREIGN KEY (genre_id) REFERENCES genres(genre_id) ON DELETE CASCADE")
print(");\n")

# **Insert Movies**
print("-- Insert movies")
for movie in movies:
    title = movie.get("Title", "Unknown").replace("'", "''")
    release_date = movie.get("Released", "")
    director = movie.get("Director", "").strip()
    genres = [genre.strip() for genre in movie.get("Genre", "").split(",")]

    # **Convert release date format**
    try:
        date_obj = datetime.strptime(release_date, "%d %b %Y")
        release_date = date_obj.strftime("%Y-%m-%d")
    except ValueError:
        release_date = None

    # **Get `director_id` from MySQL**
    director_id = director_ids.get(director, "NULL")  # If not found, store as NULL

    # **Insert Movie Query**
    release_date_value = f"'{release_date}'" if release_date else "NULL"
    print(f"INSERT INTO movies (movie_id, name, release_date, director_id) "
          f"VALUES ({next_movie_id}, '{title}', {release_date_value}, {director_id});")

    # **Insert into `movie_genres` table**
    for genre in genres:
        genre_id = genre_ids.get(genre, "NULL")  # Get genre_id from MySQL
        if genre_id != "NULL":  # Only insert if genre_id exists
            print(f"INSERT INTO movie_genres (movie_id, genre_id) "
                  f"VALUES ({next_movie_id}, {genre_id});")

    next_movie_id += 1

# **Close MySQL Connection**
cursor.close()
conn.close()
