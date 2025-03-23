from faker import Faker
import random

fake = Faker()

# Generate fake users (without password)
a=1
# for _ in range(25):
#     user_id = a
#     username = fake.user_name()
#     email = fake.email()
#     a=a+1
    
#     print(f"INSERT INTO users (user_id , username, email) VALUES ('{user_id}','{username}', '{email}');")

# Generate fake ratings
for _ in range(25):
    user_id = random.randint(1, 25)   # Assuming we have 5 users
    movie_id = random.randint(1, 250) # Assuming 10 movies
    rating = round(random.uniform(1, 10), 1)
    review = fake.sentence()

    # Escape single quotes in the review to prevent SQL errors
    review = review.replace("'", "''")

    print(f"INSERT INTO ratings (user_id, movie_id, rating, review) VALUES ({user_id}, {movie_id}, {rating}, '{review}');")
