import json

# Load JSON data
file_path = "movies-250.json"  # Change to your file path
with open(file_path, "r") as f:
    data = json.load(f)

movies = data.get("movies", [])  # Extract movie list

# Extract unique genres
genre_ids = {}
next_genre_id = 1

# Collect unique genres
for movie in movies:
    genres = [genre.strip() for genre in movie.get("Genre", "").split(",")]
    for genre in genres:
        if genre and genre not in genre_ids:
            genre_ids[genre] = next_genre_id
            next_genre_id += 1

# Print SQL queries to the terminal
print("\n-- Create genres table")
print("CREATE TABLE genres (")
print("    genre_id INT PRIMARY KEY AUTO_INCREMENT,")
print("    name VARCHAR(255) UNIQUE NOT NULL")
print(");\n")

print("-- Insert genres")
for genre, genre_id in genre_ids.items():
    print(f"INSERT INTO genres (genre_id, name) VALUES ({genre_id}, '{genre}');")
