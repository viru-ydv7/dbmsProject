# import json
# from datetime import datetime

# # Load JSON data from file
# file_path = 'movies-250.json'  # Path to your JSON file
# with open(file_path, 'r') as f:
#     data = json.load(f)

# movies = data.get('movies', [])  # Safely access movies list

# # Debug: Ensure movies are loaded
# print(f"Total movies loaded: {len(movies)}")
# if len(movies) > 0:
#     print(json.dumps(movies[:2], indent=4))  # Print first 2 movies

# # Initialize data structures
# movie_insert_queries = []
# actor_insert_queries = []
# movie_actor_insert_queries = []
# actor_ids = {}  # To store actor_id for each actor name
# next_actor_id = 1
# next_movie_id = 1

# # Helper function to convert date format
# def convert_date_format(date_string):
#     if not date_string:  # Handle missing date
#         return None
#     try:
#         date_object = datetime.strptime(date_string, "%d %b %Y")
#         return date_object.strftime("%Y-%m-%d")
#     except ValueError:
#         return None  # Return None if date format is incorrect

# # Iterate through each movie
# for movie in movies:
#     # Extract movie details
#     title = movie.get('Title', 'Unknown').replace("'", "''")
#     release_date = convert_date_format(movie.get('Released', ''))
#     genre = movie.get('Genre', 'Unknown').replace("'", "''")
#     director = movie.get('Director', 'Unknown').replace("'", "''")

#     # Debugging movie processing
#     print(f"Processing Movie ID {next_movie_id}: {title}")

#     # Create movie insert query
#     release_date_value = f"'{release_date}'" if release_date else "NULL"
#     movie_insert_query = f"""
#     INSERT INTO movies (movie_id, title, release, genre, director)
#     VALUES ({next_movie_id}, '{title}', {release_date_value}, '{genre}', '{director}');
#     """
#     movie_insert_queries.append(movie_insert_query)

#     # Extract actors and create actor insert queries
#     actors = [actor.strip() for actor in movie.get('Actors', '').split(',')]
#     for actor in actors:
#         if actor and actor not in actor_ids:  # Avoid empty actor names
#             actor_ids[actor] = next_actor_id
#             actor_insert_query = f"""
#             INSERT INTO actors (actor_id, name)
#             VALUES ({next_actor_id}, '{actor.replace("'", "''")}');
#             """
#             actor_insert_queries.append(actor_insert_query)
#             print(f"Processing Actor ID {next_actor_id}: {actor}")  # Debugging actors
#             next_actor_id += 1

#         # Create movie_actor insert query
#         if actor:
#             actor_id = actor_ids[actor]
#             movie_actor_insert_query = f"""
#             INSERT INTO movie_actors (movie_id, actor_id)
#             VALUES ({next_movie_id}, {actor_id});
#             """
#             movie_actor_insert_queries.append(movie_actor_insert_query)

#     next_movie_id += 1

# # Print all SQL queries
# print("-- Movies INSERT statements:")
# for query in movie_insert_queries[:16]:
#     print(query)

# print("\n-- Actors INSERT statements:")
# # for query in actor_insert_queries:
# #     print(query)

# print("\n-- Movie_Actors INSERT statements:")
# # for query in movie_actor_insert_queries:
# #     print(query)



import json
from datetime import datetime

# Load JSON data from file
file_path = 'movies-250.json'  # Path to your JSON file
with open(file_path, 'r') as f:
    data = json.load(f)

movies = data.get('movies', [])  # Safely access movies list

# Debug: Ensure movies are loaded
print(f"Total movies loaded: {len(movies)}")
if len(movies) > 0:
    print(json.dumps(movies[:2], indent=4))  # Print first 2 movies

# Initialize data structures
movie_insert_queries = []
actor_insert_queries = []
movie_actor_insert_queries = []
actor_ids = {}  # To store actor_id for each actor name
next_actor_id = 1
next_movie_id = 1

# Helper function to convert date format
def convert_date_format(date_string):
    if not date_string:  # Handle missing date
        return None
    try:
        date_object = datetime.strptime(date_string, "%d %b %Y")
        return date_object.strftime("%Y-%m-%d")
    except ValueError:
        return None  # Return None if date format is incorrect

# Iterate through each movie
for movie in movies:
    # Extract movie details
    title = movie.get('Title', 'Unknown').replace("'", "''")
    release_date = convert_date_format(movie.get('Released', ''))
    genre = movie.get('Genre', 'Unknown').replace("'", "''")
    director = movie.get('Director', 'Unknown').replace("'", "''")

    # Debugging movie processing
    print(f"Processing Movie ID {next_movie_id}: {title}")

    # Create movie insert query
    release_date_value = f"'{release_date}'" if release_date else "NULL"
    movie_insert_query = f"""
    INSERT INTO movies (movie_id, title, release_date, genre, director)
    VALUES ({next_movie_id}, '{title}', {release_date_value}, '{genre}', '{director}');
    """
    movie_insert_queries.append(movie_insert_query)

    # Extract actors and create actor insert queries
    actors = [actor.strip() for actor in movie.get('Actors', '').split(',')]
    for actor in actors:
        if actor and actor not in actor_ids:  # Avoid empty actor names
            actor_ids[actor] = next_actor_id
            actor_insert_query = f"""
            INSERT INTO actors (actor_id, name)
            VALUES ({next_actor_id}, '{actor.replace("'", "''")}');
            """
            actor_insert_queries.append(actor_insert_query)
            print(f"Processing Actor ID {next_actor_id}: {actor}")  # Debugging actors
            next_actor_id += 1

        # Create movie_actor insert query
        if actor:
            actor_id = actor_ids[actor]
            movie_actor_insert_query = f"""
            INSERT INTO movie_actors (movie_id, actor_id)
            VALUES ({next_movie_id}, {actor_id});
            """
            movie_actor_insert_queries.append(movie_actor_insert_query)

    next_movie_id += 1

# Print all SQL queries
print("-- Movies INSERT statements:")
for query in movie_insert_queries:  # First 16 for debugging
    print(query)

# print("\n-- Actors INSERT statements:")
# for query in actor_insert_queries:  # First 16 for debugging
#     print(query)

# print("\n-- Movie_Actors INSERT statements:")
# for query in movie_actor_insert_queries:  # First 16 for debugging
#     print(query)
