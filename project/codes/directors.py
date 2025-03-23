import json

# Load JSON data
file_path = "movies-250.json"  # Change to your file path
with open(file_path, "r") as f:
    data = json.load(f)

movies = data.get("movies", [])  # Extract movie list

# Extract unique directors
director_ids = {}
next_director_id = 1

# Collect unique directors
for movie in movies:
    director = movie.get("Director", "").strip()
    if director and director not in director_ids:
        director_ids[director] = next_director_id
        next_director_id += 1

# Print SQL queries to the terminal
print("\n-- Create directors table")
print("CREATE TABLE directors (")
print("    director_id INT PRIMARY KEY AUTO_INCREMENT,")
print("    name VARCHAR(255) UNIQUE NOT NULL")
print(");\n")

print("-- Insert directors")
for director, director_id in director_ids.items():
    print(f"INSERT INTO directors (director_id, name) VALUES ({director_id}, '{director}');")
