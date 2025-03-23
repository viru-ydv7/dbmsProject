CREATE TABLE ratings (
    user_id INT NOT NULL,
    movie_id INT NOT NULL,
    rating DECIMAL(2,1) CHECK (rating BETWEEN 0 AND 10),
    review TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id) ON DELETE CASCADE
);

INSERT INTO ratings (user_id, movie_id, rating, review) VALUES (2, 235, 9.7, 'Line adult star sea lawyer.');
INSERT INTO ratings (user_id, movie_id, rating, review) VALUES (15, 121, 5.1, 'His particularly set reveal remember story.'); 
INSERT INTO ratings (user_id, movie_id, rating, review) VALUES (9, 41, 3.9, 'Fill especially yard prove dark tend note.');    
INSERT INTO ratings (user_id, movie_id, rating, review) VALUES (19, 73, 4.4, 'East real may card wife.');
INSERT INTO ratings (user_id, movie_id, rating, review) VALUES (23, 48, 7.0, 'Politics significant live western sit suggest site.');
INSERT INTO ratings (user_id, movie_id, rating, review) VALUES (23, 215, 8.2, 'Traditional situation pass word nice none today.');
INSERT INTO ratings (user_id, movie_id, rating, review) VALUES (11, 241, 1.0, 'Involve myself even skill almost still.');     
INSERT INTO ratings (user_id, movie_id, rating, review) VALUES (13, 11, 9.9, 'Consider effect daughter personal business management various.');
INSERT INTO ratings (user_id, movie_id, rating, review) VALUES (7, 159, 3.8, 'Able near maintain beyond early.');
INSERT INTO ratings (user_id, movie_id, rating, review) VALUES (21, 212, 7.8, 'Apply government factor current.');
INSERT INTO ratings (user_id, movie_id, rating, review) VALUES (17, 9, 2.9, 'Me fish summer expect himself nation nation.');  
INSERT INTO ratings (user_id, movie_id, rating, review) VALUES (12, 22, 4.3, 'System receive environment kind.');
INSERT INTO ratings (user_id, movie_id, rating, review) VALUES (4, 29, 5.5, 'Dog growth itself state her laugh.');
INSERT INTO ratings (user_id, movie_id, rating, review) VALUES (11, 183, 5.9, 'Tough its focus face so.');
INSERT INTO ratings (user_id, movie_id, rating, review) VALUES (16, 32, 5.3, 'Place building by man size.');
INSERT INTO ratings (user_id, movie_id, rating, review) VALUES (13, 242, 4.9, 'Arrive grow law raise.');
INSERT INTO ratings (user_id, movie_id, rating, review) VALUES (7, 195, 5.7, 'Civil technology bank professional when project evening.');
INSERT INTO ratings (user_id, movie_id, rating, review) VALUES (21, 26, 5.6, 'Remember do arm trial.');
INSERT INTO ratings (user_id, movie_id, rating, review) VALUES (22, 35, 3.0, 'Word around line would.');
INSERT INTO ratings (user_id, movie_id, rating, review) VALUES (3, 11, 9.7, 'Worry these without gas.');
INSERT INTO ratings (user_id, movie_id, rating, review) VALUES (8, 204, 5.3, 'Story rather lead question water book usually.');
INSERT INTO ratings (user_id, movie_id, rating, review) VALUES (3, 35, 5.5, 'Manager anything young.');
INSERT INTO ratings (user_id, movie_id, rating, review) VALUES (3, 122, 7.3, 'Sea argue join what must help.');
INSERT INTO ratings (user_id, movie_id, rating, review) VALUES (16, 124, 2.4, 'Door tell carry medical.');
INSERT INTO ratings (user_id, movie_id, rating, review) VALUES (15, 102, 6.5, 'Decision choice design foreign although.');   